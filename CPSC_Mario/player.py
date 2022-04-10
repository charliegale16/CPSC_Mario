import pygame, time
from display import *                  # import function from file


# load sprite frames for the player animation
sprites = [pygame.image.load('images/idle.png'),
        pygame.image.load('images/runing01.png'),
        pygame.image.load('images/runing02.png')]

sprites_moving = [pygame.image.load('images/idle_rotated.png'),
                  pygame.image.load('images/runing01_rotated.png'),
                  pygame.image.load('images/runing02_rotated.png')]

jumping = [pygame.image.load('images/jumping_rotated.png'),
        pygame.image.load('images/jumping.png')]


class Player:

    def __init__(self):
        self.width  = 76
        self.height = 64
        self.x = int((Canvas.width/2) - (self.width/2))
        self.y = int(Canvas.height/1.116) - self.height

        self.xspeed = 8
        self.yspeed = 20
        self.gravity  = -1
        self.inf_limit = 600 - self.height

        self.on_ground = True
        self.rotated = False
        self.speed_animation = 0.18
        self.frame  = 0


    def jump(self):

        if self.y > self.inf_limit:
            self.y = int(600-self.height-self.yspeed)
            self.on_ground = True
            self.yspeed = 20

        self.y -= self.yspeed
        self.yspeed += self.gravity


    def collision(self, bkgd, obj):


            if (bpx < self.x and self.x < bpx + bpw or
                bpx < self.x + self.width and self.x + self.width < bpx + bpw or
                self.x < bpx and self.x + self.width > bpx + bpw):

                if bpy < self.y and self.y < bpy + bph:
                    obj.coin.pop(-c)
                    obj.qtd_coin -= 1


    def show(self, frame, rotated=False, jump=False):
        frame = int(frame)


        if jump != True:
            if rotated == True:
                Canvas.display.blit(jumping[0], (self.x, self.y))
            else:
                Canvas.display.blit(jumping[1], (self.x, self.y))
        else:
            if rotated == True:
                Canvas.display.blit(sprites_moving[frame], (self.x, self.y))
            else:
                Canvas.display.blit(sprites[frame], (self.x, self.y))

    def end(self, bkgd):
        if bkgd.x < -5145:
            pygame.quit()
