import pygame
from image import *

class Coin:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,32,32)
        self.image = load_spritesheet("assets/coin.png",32,0,32,32)
        self.velX = 1
    def update(self,dt):
        self.rect.y += self.velX*dt

    def draw(self,screen):
        screen.blit(self.image,self.rect)

