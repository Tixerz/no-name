import pygame
class enemies :
    def __init__(self,x ,y) -> None:

        self.x = x 
        self.y = y
    def move(self,toward,screen):
        surface = pygame.Surface((10,10))
        surface.fill("Red")
        if toward == "w"  :
            self.y -= 1
            if self.y <=0 :
                self.y = 10
            screen.blit(surface , (self.x,self.y))
            pygame.display.update()
        elif toward == "s" :
            self.y += 1
            if self.y >= 390: 
                self.y = 390
            screen.blit(surface , (self.x,self.y))
            pygame.display.update()
        elif toward == "d" :
            self.x+=1
            if self.x > 800 :
                self.x = 800
            screen.blit(surface , (self.x,self.y))
            pygame.display.update()
        elif toward == "a" :
            self.x -=1
            if self.x < 0 :
                self.x = 10
            screen.blit(surface , (self.x,self.y))
            pygame.display.update()
