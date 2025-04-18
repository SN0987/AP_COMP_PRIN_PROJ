import pygame


class Tile:
    def __init__(self,x,y,size):
        self.rect = pygame.Rect(x,y,size,size)
        self.image = pygame.image.load("assets/tile.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(size,size))
    def update(self,dt):
        pass

    def draw(self,screen):
        screen.blit(self.image,self.rect)