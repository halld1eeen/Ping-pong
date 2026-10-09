from pygame import *


win = display.set_mode((700,500))
back=transform.scale(image.load('i.png'),(700,500))


class GameSprite(sprite.Sprite):
    def __init__(self,sprite,speed,rect_x,rect_y,wid,hei):
        super().__init__()
        self.image=transform.scale(image.load(sprite),(hei,wid))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=rect_x
        self.rect.y=rect_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys=key.get_pressed()

        if keys[K_s] and self.rect.y<400:
            self.rect.y+=self.speed
        if keys[K_w] and self.rect.y>20:
            self.rect.y-=self.speed

    def update_l(self):
        keys=key.get_pressed()

        if keys[K_DOWN] and self.rect.y<400:
            self.rect.y+=self.speed
        if keys[K_UP] and self.rect.y>20:
            self.rect.y-=self.speed

class Ball(GameSprite):
    def update(self):
        pass

fps=60
timer=time.Clock()

finish=False

font.init()
font1=font.SysFont('Arial',50)

lose1=font1.render('ИГРОК 1 ПРОИГРАЛ!',True,(255,0,0))
lose2=font1.render('ИГРОК 2 ПРОИГРЫВАЕТ!',True,(255,0,0))

right=Player('правая.png',4,0,200,100,190)
left=Player('левая.png',4,500,200,100,190)
ball=Ball('мячик.png',3,300,200,60,60)

speed_x=3
speed_y=3

game=True
while game:
    timer.tick(fps)
    win.blit(back,(0,0))
    for e in event.get():
        if e.type==QUIT:
            game=False

    right.reset()
    right.update_r()

    left.reset()
    left.update_l()

    ball.reset()
    ball.update()

    ball.rect.x+=speed_x
    ball.rect.y+=speed_y

    if ball.rect.y>=450 or ball.rect.y<0:
        speed_y*=-1

    if sprite.collide_rect(right,ball):
        speed_x*=-1
    if sprite.collide_rect(left,ball):
        speed_x*=-1


    if ball.rect.x>=700:
        finish=True
        win.blit(lose2,(90,230))
    if ball.rect.x<=0:
        finish=True
        win.blit(lose1,(90,230))

    display.update()