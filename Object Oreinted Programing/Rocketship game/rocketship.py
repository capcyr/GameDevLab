import pygame
from pygame.locals import *
from time import *
pygame.init()
screen = pygame.display.set_mode((600,600))
playerx = 200
playery = 200

record = [False,False,False,False]

space = pygame.image.load("space.jpg")
rocketship = pygame.image.load("rocketship.png")
while playery<600:
    screen.blit(space,(0,0))
    screen.blit(rocketship,(playerx,playery))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                record[0]=True
            elif event.key == K_LEFT:
                record[1]=True
            elif event.key == K_DOWN:
                record[2]=True
            elif event.key == K_RIGHT:
                record[3]=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                record[0]=False
            elif event.key == pygame.K_LEFT:
                record[1]=False
            elif event.key == pygame.K_DOWN:
                record[2]=False
            elif event.key == pygame.K_RIGHT:
                record[3]=False
    if record[0]:
        if playery > 0:
            playery-=40
    if record[2]:
        if playery < 600:
            playery+=25
    if record[3]:
        if playerx < 600:
            playerx+=25
    if record[1]:
        if playerx > 0:
            playerx-=25
        
    playery+=15
    sleep(0.25)
    #pygame.display.update()

