import pygame
from Tile import * 
from globalsv import * 

class World:
    def __init__(self,map,row,column):
        self.tiles = []

        self.row = 0
        self.column = 0
        for i in range(column):
            for j in range(row):
                if map[i][j] == 1:
                    self.tiles.append(Tile(j*TILE_SIZE,i*TILE_SIZE,TILE_SIZE))


                


    def update(self,dt):
        for i in range(len(self.tiles)):
            self.tiles[i].update(dt)

    def draw(self,screen):
        for i in range(len(self.tiles)):
            self.tiles[i].draw(screen)