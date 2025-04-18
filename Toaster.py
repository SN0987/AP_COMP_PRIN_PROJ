import pygame
import random
from globalsv import * 

class Toaster:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,108,64)
        self.image = pygame.image.load("assets/toaste.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(128,128))

        self.chance = random.randrange(1,3)
        if self.chance == 1:
            self.speed = 1
        else:
            self.speed = -1

        
    def update(self,dt):
        self.rect.x+=self.speed*dt 

        if self.rect.x <= 0:
            self.speed*=-1
        
        if self.rect.x >= WIDTH-self.rect.w:
            self.speed*=-1


    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,255),self.rect)
        screen.blit(self.image,(self.rect.x-9,self.rect.y-36))