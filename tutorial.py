import pygame
pygame.init()
win = pygame.display.set_mode((1100,600))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

walkRight1 = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
walkLeft1 = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]

bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

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
        self.health = 20
        self.visible = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    def draw(self,win):
        if self.visible:
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
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 20))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 20))


            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    def draw1(self,win):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if not(self.standing):
                if self.left:
                    win.blit(walkLeft1[self.walkCount//3],(self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight1[self.walkCount//3],(self.x,self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(walkRight1[0],(self.x,self.y))
                else:
                    win.blit(walkLeft1[0],(self.x,self.y))
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 20))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 20))

            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            pygame.init()
        print("hit")
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.hitbox = (self.x, self.y, 10, 10)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.hitbox = (self.x, self.y-5, 10, 10)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    def hit(self):
        print("Collide")
def redrawGameWindows():
    win.blit(bg,(0,0))
    player1.draw(win)
    player2.draw1(win)
    for bullet in bullets1:
        bullet.draw(win)
    for bullet2 in bullets2:
        bullet2.draw(win)
    pygame.display.update()
player1 = player(1000,450,64,64)
player2 = player(100,450,64,64)
bullets1 = []
bullets2 = []
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets1:
        if bullet.y - bullet.radius < player2.hitbox[1] + player2.hitbox[3] and bullet.radius + bullet.y > player2.hitbox[1]:
            if bullet.x + bullet.radius > player2.hitbox[0] and bullet.x - bullet.radius < player2.hitbox[0] + player2.hitbox[2]:
                player2.hit()
                bullets1.pop(bullets1.index(bullet))
        
        if bullet.x < 1100 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets1.pop(bullets1.index(bullet))
    #BULLETS COLLISIONS SECTIONS
    for bullet in bullets1:
        for bullet2 in bullets2:
          if bullet.y - bullet.radius < bullet2.hitbox[1] + bullet2.hitbox[3] and bullet.radius + bullet.y > bullet2.hitbox[1]:
            if bullet.x + bullet.radius > bullet2.hitbox[0] and bullet.x - bullet.radius < bullet2.hitbox[0] + bullet2.hitbox[2]:
                bullet2.hit()
                bullets1.pop(bullets1.index(bullet))
                bullets2.pop(bullets2.index(bullet2))
    for bullet2 in bullets2:
        if bullet2.y - bullet2.radius < player1.hitbox[1] + player1.hitbox[3] and bullet2.radius + bullet2.y > player1.hitbox[1]:
            if bullet2.x + bullet2.radius > player1.hitbox[0] and bullet2.x - bullet2.radius < player1.hitbox[0] + player1.hitbox[2]:
                player1.hit()
                bullets2.pop(bullets2.index(bullet2))
        
        if bullet2.x < 1100 and bullet2.x > 0:
            bullet2.x += bullet2.vel
        else:
            bullets2.pop(bullets2.index(bullet2))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        bulletSound.play()
        if player1.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets1) < 5:
            bullets1.append(projectile(round(player1.x + player1.width //2), round(player1.y + player1.height//2), 6, (0,0,255), facing))

    
    if keys[pygame.K_LEFT] and player1.x > -20:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
        player1.standing = False
    elif keys[pygame.K_RIGHT] and player1.x < 1100 - player1.width-player1.vel:
        player1.x += player1.vel
        player1.right = True
        player1.left = False
        player1.standing = False
    else:
        player1.standing = True
        player1.walkCount = 0
    if not(player1.isJump):
        if keys[pygame.K_UP]:
            player1.isJump = True
            player1.right = False
            player1.Left = False
            player1.walkCount = 0
    else:
        if player1.jumpCount >= -5:
            neg = 1
            if player1.jumpCount < 0:
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
            player1.jumpCount -= 1
        else:
            player1.isJump = False
            player1.jumpCount = 5
    if not(player1.isJump1):
        if keys[pygame.K_RSHIFT]:
            player1.isJump1 = True
            player1.right = False
            player1.Left = False
            player1.walkCount = 0
    else:
        if player1.jumpCount1 >= -10:
            neg = 1
            if player1.jumpCount1 < 0:
                neg = -1
            player1.y -= (player1.jumpCount1 ** 2) * 0.5 * neg
            player1.jumpCount1 -= 1
        else:
            player1.isJump1 = False
            player1.jumpCount1 = 10
       

#for second player
    if keys[pygame.K_SPACE]:
        bulletSound.play()
        if player2.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets2) < 5:
            bullets2.append(projectile(round(player2.x + player2.width //2), round(player2.y + player2.height//2), 6, (255,0,0), facing))

    if keys[pygame.K_a] and player2.x > -20:
        player2.x -= player2.vel
        player2.left = True
        player2.right = False
        player2.standing = False
    elif keys[pygame.K_d] and player2.x < 1100 - player2.width-player2.vel:
        player2.x += player2.vel
        player2.right = True
        player2.left = False
        player2.standing = False
    else:
        player2.standing = True
        player2.walkCount = 0
    if not(player2.isJump):
        if keys[pygame.K_w]:
            player2.isJump = True
            player2.right = False
            player2.Left = False
            player2.walkCount = 0
    else:
        if player2.jumpCount >= -5:
            neg = 1
            if player2.jumpCount < 0:
                neg = -1
            player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
            player2.jumpCount -= 1
        else:
            player2.isJump = False
            player2.jumpCount = 5
    if not(player2.isJump1):
        if keys[pygame.K_e]:
            player2.isJump1 = True
            player2.right = False
            player2.Left = False
            player2.walkCount = 0
    else:
        if player2.jumpCount1 >= -10:
            neg = 1
            if player2.jumpCount1 < 0:
                neg = -1
            player2.y -= (player2.jumpCount1 ** 2) * 0.5 * neg
            player2.jumpCount1 -= 1
        else:
            player2.isJump1 = False
            player2.jumpCount1 = 10
    
    redrawGameWindows()
pygame.quit()
