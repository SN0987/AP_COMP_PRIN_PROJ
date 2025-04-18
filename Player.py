import pygame
from image import *
from pygame.locals import *
from globalsv import * 
class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,32,56)
        self.images = []

        self.state = "idle"

        self.jump = False
        self.is_grounded = False

        self.frame = 0

        self.jump_counter = 0 
        self.jumpSpeed = 7
        
        jump_images = []
        run_images = []
        for i in range(5):
 
            image = load_spritesheet("assets/potato.png",i*32,0,32,32).convert_alpha()
            image = pygame.transform.scale(image,(64,64))
            jump_images.append(image)
         

        for i in range(4):
           
            image = load_spritesheet("assets/potato.png",i*32,32,32,32).convert_alpha()
            image = pygame.transform.scale(image,(64,64))
            run_images.append(image)
        

        self.images = [jump_images,run_images]


        self.counter = 0

        self.velX = 0
        self.velY = 0
       
        self.gravity = 3.5
    
    def update(self,dt,toaster):
        
        self.key = pygame.key.get_pressed()


        #x
        if self.key[pygame.K_a]:
            self.velX = -4
    

            if not self.state == "jumping": 
                self.state = "running"
            self.state = "running" 
        elif self.key[pygame.K_d]:
            self.velX = 4
            
            if not self.state == "jumping":
                self.state = "running"
        else:
            self.velX = 0

            if not self.state == "jumping":
                self.state = "idle"

        if self.rect.x >= WIDTH-self.rect.w:
            self.rect.x = WIDTH-self.rect.w


        if self.rect.x <= 0:
            self.rect.x = 0

        if self.state == "running":
            self.counter+=dt
            if self.counter >= 1/6:
                self.counter = 0
                if self.frame >= 3:
                    self.frame = 0 
                else:
                    self.frame+=1


        
        self.rect.x += self.velX * dt

        if self.rect.colliderect(toaster.rect):
            if self.velX >= 0:
                self.rect.x = toaster.rect.x - self.rect.w 
                self.velX = toaster.speed

            if self.velX <= 0:
                self.rect.x = toaster.rect.right
                self.velX = toaster.speed 
        #y

        if not self.is_grounded and self.jump == False:
            self.velY = self.gravity


        if self.key[pygame.K_SPACE]:
            if not self.jump and self.is_grounded:
                self.jump = True 
                self.is_grounded = False
                self.state = "jumping"
                

        
        if self.state == "jumping":
            self.counter += dt 
            if self.counter >= 1/3:
                self.counter = 0
                if self.frame >= 4:
                    self.frame =0 
                else:
                    self.frame+=1  
  

        
        if self.jump:
            self.velY = -self.jumpSpeed

            self.jump_counter+=1 
           

            if self.jump_counter >= 50:
                self.jump = False 
        
        if self.jump_counter >= 50 and self.jump == False:
            self.jump_counter = 0
            self.state = "idle"

        self.rect.y += self.velY * dt

        if self.rect.colliderect(toaster.rect):
            if self.velY >= 0:
                self.is_grounded = True 
                self.rect.y = toaster.rect.y-self.rect.h
              
             
            if self.velY <= 0:
                self.rect.y = toaster.rect.bottom 
        else:
            self.is_grounded = False 
        


    def draw(self,screen):
        #pygame.draw.rect(screen,(255,0,0),(self.rect))
        #screen.blit(self.images[0][0],(self.rect.x-15,self.rect.y-8))

        if self.state == "idle":
            screen.blit(self.images[0][0],(self.rect.x-15,self.rect.y-8))

        if self.state == "running":
        

            screen.blit(self.images[1][self.frame],(self.rect.x-15,self.rect.y-8)) 

        if self.state == "jumping":
        

            screen.blit(self.images[0][self.frame],(self.rect.x-15,self.rect.y-8)) 

            
            