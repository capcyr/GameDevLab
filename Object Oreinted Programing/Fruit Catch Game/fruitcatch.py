import pygame
import time
import random
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((1000,750))
run = True
scoringfont = pygame.font.SysFont("Calibri",size = 50)

background = pygame.image.load("images/appletree.jpg")
apple = pygame.image.load("images/apple.png")
basket = pygame.image.load("images/basket.png")
lemon = pygame.image.load("images/lemon.png")
orange = pygame.image.load("images/orange.png")
watermelon = pygame.image.load("images/watermelon.png")
scoring = 0

while run:
    screen.blit(background,(0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()
