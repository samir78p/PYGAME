import pygame
pygame.init()
win = pygame.display.set_mode((850,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')
#music = pygame.mixer.music.load('music.mp3')
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self. vel = 5
        self.isJump = False
        self.right = False
        self.left = False
        self.walkCount = 0
        self.jumpCount = 5
        self.jumpCount1 = 10
        self.isJump1 = False
        self.standing = True
    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            elif self.left:
                win.blit(walkLeft[0],(self.x,self.y))
            else:
                win.blit(char,(self.x,self.y))
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = facing * 10
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.width = width
        self.height = height
        self.end = end
        self.path = [x,end]
        self.walkCount = 0
        self.vel = 3
    def draw(self,win):
        self.mov()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
    def mov(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
                self.left = False
                self.right = True
            else:

                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
                self.left = True
                self.right = False
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
    def shoot(self):
        for bullet in Gbullets:
            if bullet.x < 450 and bullet.x > 0:
                bullet.x += bullet.vel
        if self.left:
            facing
def redrawGameWindows():
    win.blit(bg,(0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
man = player(200,410,64,64)
Gbullets = []
bullets = []
goblin = enemy(100,417,64,64,850)
run = True
while run:
    clock.tick(27)
    for bullet in bullets:
        if bullet.x < 850 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
    if keys[pygame.K_LEFT] and man.x > -20:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 870 - man.width-man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.Left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -5:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 5
    if not(man.isJump1):
        if keys[pygame.K_TAB]:
            man.isJump1 = True
            man.right = False
            man.Left = False
            man.walkCount = 0
    else:
        if man.jumpCount1 >= -10:
            neg = 1
            if man.jumpCount1 < 0:
                neg = -1
            man.y -= (man.jumpCount1 ** 2) * 0.5 * neg
            man.jumpCount1 -= 1
        else:
            man.isJump1 = False
            man.jumpCount1 = 10
    redrawGameWindows()
pygame.quit()
            
