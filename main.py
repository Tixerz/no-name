import pygame
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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] == 1 :
        if playery+1 < 390 :
            playery +=1
    if keys[pygame.K_d] ==1 :
        if playerx+1 < 790 :
            playerx +=1
    if keys[pygame.K_a] == 1:
        if playerx-1 >0:
            playerx -=1
    if keys[pygame.K_w] ==1 :
        if playery-1 > 0:
            playery -=1
    #dash
    if keys[pygame.K_w] and keys[pygame.K_SPACE]==1:

        playery -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()

    if keys[pygame.K_a] and keys[pygame.K_SPACE]==1:

        playerx -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playerx -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playerx -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playerx -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playerx -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()

    if keys[pygame.K_s] and keys[pygame.K_SPACE]==1:

        playery += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()

    if keys[pygame.K_d] and keys[pygame.K_SPACE]==1:

        playerx += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playerx += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playerx += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playerx += 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()
        playery -= 10
        window.blit(player  , (playerx, playery))
        pygame.display.update()


    window.blit(refresh_surface,(0,0))
    window.blit(player  , (playerx, playery))
    
    pygame.display.update()
    clock.tick(1000)
