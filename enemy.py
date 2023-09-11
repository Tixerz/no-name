import pygame
class enemies :
    def __init__(self,x ,y) -> None:

        self.x = x 
        self.y = y
    def move(self,toward,screen):
        
        self.surface = pygame.Surface((10,10))
        self.surface.fill("Red")
        self.rect = pygame.Rect(self.x,self.y, 10,10)
        if toward == "w"  :
            self.y -= 1
            self.rect = pygame.Rect(self.x,self.y, 10,10)
            if self.y <=0 :
                self.y = 10
            screen.blit(self.surface , (self.x,self.y))
            pygame.display.update()
        elif toward == "s" :
            self.y += 1
            self.rect = pygame.Rect(self.x,self.y, 10,10)
            if self.y >= 390: 
                self.y = 390
            screen.blit(self.surface , (self.x,self.y))
            pygame.display.update()
        elif toward == "d" :
            self.x+=1
            self.rect = pygame.Rect(self.x,self.y, 10,10)
            if self.x > 800 :
                self.x = 800
            screen.blit(self.surface , (self.x,self.y))
            pygame.display.update()
        elif toward == "a" :
            self.x -=1
            self.rect = pygame.Rect(self.x,self.y, 10,10)
            if self.x < 0 :
                self.x = 10
            screen.blit(self.surface , (self.x,self.y))
            pygame.display.update()
    def Follow(self,playerx , playery, screen):
        self.surface = pygame.Surface((10,10))
        self.surface.fill("Red")
        self.rect = pygame.Rect(self.x,self.y, 10,10)
        if playerx > self.x :
            self.x +=3
        else:
            self.x -= 3
        if playery > self.y :
            self.y +=3
        else :
            self.y -= 3
        screen.blit(self.surface , (self.x,self.y))
        pygame.display.update()