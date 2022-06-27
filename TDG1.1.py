import pygame
import os

pygame.init()
win_width=700
win_height=400
win=pygame.display.set_mode((win_width,win_height))

stationary=pygame.image.load(os.path.join("Hero","standing.png"))
left=[pygame.image.load(os.path.join("Hero","L1.png")),
      pygame.image.load(os.path.join("Hero","L2.png")),
      pygame.image.load(os.path.join("Hero","L3.png")),
      pygame.image.load(os.path.join("Hero","L4.png")),
      pygame.image.load(os.path.join("Hero","L5.png")),
      pygame.image.load(os.path.join("Hero","L6.png")),
      pygame.image.load(os.path.join("Hero","L7.png")),
      pygame.image.load(os.path.join("Hero","L8.png")),
      pygame.image.load(os.path.join("Hero","L9.png"))]

right=[pygame.image.load(os.path.join("Hero","R1.png")),
       pygame.image.load(os.path.join("Hero","R2.png")),
       pygame.image.load(os.path.join("Hero","R3.png")),
       pygame.image.load(os.path.join("Hero","R4.png")),
       pygame.image.load(os.path.join("Hero","R5.png")),
       pygame.image.load(os.path.join("Hero","R6.png")),
       pygame.image.load(os.path.join("Hero","R7.png")),
       pygame.image.load(os.path.join("Hero","R8.png")),
       pygame.image.load(os.path.join("Hero","R9.png"))]
unscaled_background=pygame.image.load("desert_BG.png")
background=pygame.transform.scale(unscaled_background,(win_width,win_height))
unscaled_bullet=pygame.image.load("bullet.png")
bullet_img=pygame.transform.scale(unscaled_bullet,(10,10))
class Hero():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.velx=10
        self.vely=10
        self.faceRight=True
        self.faceLeft=False
        self.jump=False
        self.stepIndex=0
        self.bullets=[]
        
    def move_hero(self,userInput):
        if userInput[pygame.K_RIGHT] and self.x<=660:
            self.x+=self.velx
            self.faceRight=True
            self.faceLeft=False
        elif userInput[pygame.K_LEFT] and self.x>=0:
            self.x-=self.velx
            self.faceRight=False
            self.faceLeft=True
        else:
            self.stepIndex=0

    def jump_motion(self,userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump=True
        if self.jump:
            self.y-=self.vely*4
            self.vely-=1
        if self.vely<-10:
            self.jump=False
            self.vely=10

    def draw(self,win):
        if self.stepIndex>=9:
            self.stepIndex=0
        if self.faceRight:
            win.blit(right[self.stepIndex],(self.x,self.y))
            self.stepIndex+=1
        elif self.faceLeft:
            win.blit(left[self.stepIndex],(self.x,self.y))
            self.stepIndex+=1

    def direction(self):
        if self.faceRight:
            return 1
        if self.faceLeft:
            return -1

    def shoot(self):
        if userInput[pygame.K_f]:
            bullet=Bullet(self.x,self.y,self.direction())
            self.bullets.append(bullet)
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

class Bullet():
    def __init__(self,x,y,direction):
        self.x=x
        self.y=y
        self.direction=direction

    def draw_bullet(self):
        win.blit(bullet_img,(self.x,self.y))

    def move(self):
        if self.direction==1:
            self.x+=15
        if self.direction==-1:
            self.x-=15

    def off_screen(self):
        return not(self.x>=0 and self.x<=win_width)

def draw_game():
    win.fill((0,0,0))
    win.blit(background,(0,0))
    player.draw(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    pygame.time.delay(50)
    pygame.display.update()

player=Hero(350,300)

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    userInput=pygame.key.get_pressed()
    player.move_hero(userInput)
    player.jump_motion(userInput)
    player.shoot()
    draw_game()
