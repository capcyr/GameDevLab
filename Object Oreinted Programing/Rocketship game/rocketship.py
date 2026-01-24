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
    screen.blit(rocketship,(250,250))
    
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

    pygame.display.update()
