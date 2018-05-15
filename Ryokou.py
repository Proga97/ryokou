import pygame as p
import spritesheet
import math

class Hero(object):

    def __init__(self,state):
        self.speed=30
        self.jumpspeed=35
        self.flip=p.transform.flip
        self.STATE=state
        ss=spritesheet.spritesheet("hero.png")
        self.images=ss.images_at([(40,50,179,211),(280,63,224,203),(506,48,387,229),(892,68,388,220),(2,304,425,195),(425,319,220,177)],colorkey=(255,255,255))
        self.run_images=ss.images_at([(437,510,150,155),(589,510,150,155),(763,510,150,155),(951,510,150,155),(159,666,150,155),
                                      (314, 666, 150, 155),(464,666,150,155),(613,666,150,155),(777,666,150,155),(935,666,150,155),
                                      (170, 853, 150, 155),(326, 853, 150, 155),(475, 853, 150, 155),(636, 853, 150, 155),
                                      (790, 853, 150, 155),(965, 853, 150, 155)],colorkey=(255,255,255))

        self.jump_images=ss.images_at([(682,309,100,190),(828,309,100,190),(1005,309,100,190),(1128,309,100,190)])
        self.image=None
        self.counter=0
        self.runcounter=0
        self.jumpcounter=0
        self.direction="right"
        self.vertical="down"
    def action(self,pos):
        global  screen



        if self.STATE=="idle":
            if self.direction=="right":
                screen.blit(self.flip(self.images[0],True,False),pos)
            else:
                screen.blit(self.flip(self.images[0], False, False), pos)
            return



        if self.STATE=="attack":
            print "ATTACKING"
            if self.direction=="right":
                if self.counter>=len(self.images):
                    self.counter=0
                    self.STATE="idle"

                screen.blit(self.flip(self.images[int(math.floor(self.counter))],True,False),pos)
                self.counter+=0.5
            if self.direction=="left":
                if self.counter >= len(self.images):
                    self.counter = 0
                    self.STATE = "idle"

                screen.blit(self.flip(self.images[int(math.floor(self.counter))], False, False), pos)
                self.counter += 0.5




        if self.STATE=="running":
            if self.direction=="left":
                if self.runcounter>=len(self.run_images):
                    self.runcounter=0
                pos[0]-=self.speed
                screen.blit(self.flip(self.run_images[self.runcounter],False,False),pos)
                self.runcounter+=1
            if self.direction=="right":
                if self.runcounter>=len(self.run_images):
                    self.runcounter=0
                pos[0]+=self.speed
                screen.blit(self.flip(self.run_images[self.runcounter],True,False),pos)

                self.runcounter+=1
        if self.STATE=="jump":
            if self.vertical=="up":
                pos[1]-=self.jumpspeed
                self.jumpcounter+=1
            if self.vertical=="down":
                pos[1]+=self.jumpspeed
                self.jumpcounter-=1
            if self.direction=="left":
                if self.jumpcounter>=len(self.jump_images):
                    self.jumpcounter=len(self.jump_images)-1
                    self.vertical="down"
                if self.jumpcounter<0:
                    self.jumpcounter=0
                    self.STATE="idle"
                    print self.STATE
                    pos[1]+=self.jumpspeed
                    return

                screen.blit(self.flip(self.jump_images[self.jumpcounter],False,False),pos)


            if self.direction=="right":
                if self.jumpcounter>=len(self.jump_images):
                    self.jumpcounter=len(self.jump_images)-1
                    self.vertical="down"
                if self.jumpcounter<0:
                    self.jumpcounter=0
                    self.STATE="idle"
                    print self.STATE
                    pos[1] += self.jumpspeed
                    return
                print pos
                screen.blit(self.flip(self.jump_images[self.jumpcounter],True,False),pos)



    def attack(self):
        self.STATE="attack"

    def run(self,direction):
        self.direction=direction
        self.STATE="running"

    def stop_run(self):
        self.STATE="idle"
        self.runcounter=0

    def jump(self):
        self.vertical="up"
        self.STATE="jump"
        self.jumpcounter=-1



p.init()
Res = (1280, 768)
screen = p.display.set_mode(Res)
clock = p.time.Clock()
bg_image = p.image.load("lol.jpg").convert()
bg_image=p.transform.scale(bg_image,Res)

pos=[1280/2,768/2]
ryouku=Hero("idle")
print pos
while True:

    for event in p.event.get():

        if event.type==p.KEYDOWN:
            if event.key==p.K_a:
                ryouku.run("left")
            if event.key==p.K_d:
                ryouku.run("right")
            if event.key==p.K_w:
                ryouku.jump()
        if event.type==p.KEYUP:
            if ryouku.STATE=="running":
                ryouku.stop_run()
        if event.type == p.MOUSEBUTTONDOWN:
            if event.button==1:

                ryouku.attack()

    ryouku.action(pos)
    clock.tick(30)

    p.display.flip()
    screen.fill((255,255,255))



