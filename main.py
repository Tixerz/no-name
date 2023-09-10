import pygame
import math
from sys import exit
pygame.init()
window = pygame.display.set_mode((800,400))
pygame.display.set_caption("Petrix")
clock = pygame.time.Clock()                           
refresh_surface = pygame.Surface((800,400))
refresh_surface.fill("Black")

player = pygame.Surface((10,10))
player.fill("White")
playerx= 2
playery=2
counter2 = 0
counter = 0 
def dash_anim(x , y , bool):
    if x != 0 and y != 0 :
        x= x *math.sin(45)
        y = y*math.sin(45)
    global counter
    global playerx
    global playery
    if counter >= 240 : 
        if bool == True:
            playerx += x 
            playery += y
           

            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()
            playerx += x 
            playery += y
            window.blit(player  , (playerx, playery))
            pygame.display.update()

            if playerx >= 790 :
                playerx = 790
            if playery >=390 :
                playery = 390
            if playerx < 10 :
                playerx = 10
            if playery <= 10 :
                playery =10
            counter = 0 
    
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] == 1 :
        if playery+1 < 390 :
            window.blit(player  , (playerx, playery))
            playery +=1
            window.blit(player  , (playerx, playery))
            playery +=1
            window.blit(player  , (playerx, playery))
    if keys[pygame.K_d] ==1 :
        if playerx+1 < 790 :
            window.blit(player  , (playerx, playery))
            playerx +=1
            window.blit(player  , (playerx, playery))
            playerx +=1
            window.blit(player  , (playerx, playery))
    if keys[pygame.K_a] == 1:
        if playerx-1 >0:
            window.blit(player  , (playerx, playery))
            playerx -=1
            window.blit(player  , (playerx, playery))
            playerx -=1
            window.blit(player  , (playerx, playery))
    if keys[pygame.K_w] ==1 :
        if playery-1 > 0:
            window.blit(player  , (playerx, playery))
            playery -=1
            window.blit(player  , (playerx, playery))
            playery -=1
            window.blit(player  , (playerx, playery))
            




    #dash
    counter += 10
 

    dash_anim(6  ,-6 , keys[pygame.K_w]and keys[pygame.K_d] and keys[pygame.K_SPACE] == 1) 
    dash_anim(-6 , -6 , keys[pygame.K_w]and keys[pygame.K_a] and keys[pygame.K_SPACE] == 1)
    dash_anim(6 , 6 , keys[pygame.K_s]and keys[pygame.K_d] and keys[pygame.K_SPACE] == 1)
    dash_anim(-6 , 6 , keys[pygame.K_s]and keys[pygame.K_a] and keys[pygame.K_SPACE] == 1)

    dash_anim(-6 , 0 , keys[pygame.K_a]and keys[pygame.K_SPACE] == 1)   
    dash_anim(0 , 6 , keys[pygame.K_s]and keys[pygame.K_SPACE] == 1) 
    dash_anim(6 , 0 , keys[pygame.K_d]and keys[pygame.K_SPACE] == 1)
    dash_anim( 0, -6 , keys[pygame.K_w]and keys[pygame.K_SPACE] == 1)

    counter2 += 10
    if counter2 >= 90:
        window.blit(refresh_surface , (0,0))
        counter2 = 0
    window.blit(player  , (playerx, playery))
    pygame.display.update()
    clock.tick(90)

