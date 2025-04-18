import pygame,sys,random
from Player import *
from globalsv import *
from world import * 
from Toaster import *
from Coins import * 
from text import * 
pygame.init()


      

class Game:
    def __init__(self,width,height,fps,title):
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
        self.fps = fps 
        self.width = width 
        self.height = height 

        self.game_state = "Menu"
        self.coins = []
        self.insertTime = 5
        self.score = 0

        self.main_game()
     

    def main_game(self):
        
        m = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]

        isRunning = True 

        currentTime =0 
        dt = 0
        lastTime =0
    


        world = World(m,32,19)
        toaster = Toaster(WIDTH/2-64,HEIGHT-116)
        player = Player(WIDTH/2-32,HEIGHT-(116+64))

   
        coinCounter = 0

        changeInsertTime = 0

        lostTime = 0
        lostTimeTwo = 5

        scoreText = Text("assets/font_pixel.ttf","Score: 0",30,(200,200,200))

        winTime = 0
        winTimeTwo = 5

        seconds = 0
        lostTexts = [
            Text("assets/font_pixel.ttf","YOU LOST!",120,(200,200,200)),
            Text("assets/font_pixel.ttf","YOU WILL GO BACK IN 5",80,(200,200,200))
        ]

        menuTexts = [
            Text("assets/font_pixel.ttf","Potato Man!",150,(200,200,200)),
            Text("assets/font_pixel.ttf","Click Enter To Play!",60,(200,200,200))
        ]

        winTexts = [
            Text("assets/font_pixel.ttf","YOU WIN!",120,(200,200,200)),
            Text("assets/font_pixel.ttf","YOU WILL GO BACK IN 5",80,(200,200,200))
        ]

        
        while isRunning:
            currentTime = pygame.time.get_ticks()
            dt = (currentTime-lastTime)/1000
            dt*=self.fps
            lastTime = currentTime 
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if self.game_state == "Menu":
                        if event.key == pygame.K_RETURN:
                            self.game_state = "Game"

                    if self.game_state == "Game":
                        pass
            

            if self.game_state == "Menu" :
                self.screen.fill((35,35,35))

                menuTexts[0].draw(self.screen,189,50)
                menuTexts[1].draw(self.screen,260,HEIGHT-100)
            
            elif self.game_state == "Game":
                self.screen.fill((35,35,35))


    
   
            
                world.update(dt)
                toaster.update(dt)
                player.update(dt,toaster)


            

                coinCounter+= dt 

                if coinCounter >= 120*self.insertTime:
                    coinCounter = 0
                    self.coins.append(Coin(toaster.rect.x,-32))

                changeInsertTime+=dt 

                if changeInsertTime >= 120*60:
                    if self.insertTime > 2:
                        self.insertTime-=1 

                        
                for i in range(len(self.coins)):
                    self.coins[i].update(dt)

                for i in range(len(self.coins)):
                    if self.coins[i].rect.y >= HEIGHT:
                        self.reset_game(player,toaster,scoreText)
                        self.game_state = "Lose"
                    if self.coins[i].rect.colliderect(player.rect):
                        del self.coins[i]
                        self.score+=1

                        scoreText.setText("Score: " + str(self.score))
                   

                
                if player.rect.y >= HEIGHT:
                    self.reset_game(player,toaster,scoreText)
                    self.game_state = "Lose"

                if self.score >= 100:
                    self.reset_game(player,toaster,scoreText)
                    self.game_state = "Win"
                scoreText.draw(self.screen,30,30)
                world.draw(self.screen)
                toaster.draw(self.screen)
                player.draw(self.screen)

                for i in range(len(self.coins)):
                    self.coins[i].draw(self.screen)
            elif self.game_state == "Lose":
                self.screen.fill((35,35,35))

                lostTime += dt 

                seconds+=dt 
                if seconds >= self.fps:
                    seconds = 0
                    lostTimeTwo-=1
                    lostTexts[1].setText("YOU WILL GO BACK IN " + str(lostTimeTwo))
                if lostTime >= 5*120:
                    self.game_state = "Menu"
                    lostTime = 0
                    lostTimeTwo = 5

                
                
                lostTexts[0].draw(self.screen,290,160)
                lostTexts[1].draw(self.screen,175,280)
                    

            elif self.game_state == "Win":
                self.screen.fill((35,35,35))
                winTime += dt 

                seconds+=dt 
                if seconds >= self.fps:
                    seconds = 0
                    winTimeTwo-=1
                    winTexts[1].setText("YOU WILL GO BACK IN " + str(winTimeTwo))

                if winTime >= 5*120:
                    self.game_state = "Menu"
                    winTime = 0
                    winTimeTwo = 5

                
                
                winTexts[0].draw(self.screen,300,160)
                winTexts[1].draw(self.screen,175,280)



            pygame.display.update()
            pygame.time.Clock().tick(self.fps)

    def reset_game(self,player,toaster,score_text):
        toaster.rect.x = WIDTH/2-64
        toaster.rect.y = HEIGHT-116
        player.rect.x = WIDTH/2-32
        player.rect.y = HEIGHT-(116+64)
        score_text.setText("Score: " + str(0))
        self.coins.clear()
        self.insertTime = 5 
        self.score = 0
        
     

if __name__ == "__main__" :
    game = Game(WIDTH,HEIGHT,120,"POTATO MAN") 
