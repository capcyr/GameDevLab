import pygame
import random
import time

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((500,800))
pygame.display.set_caption("Car Game")

road = pygame.image.load("./images/road.png")

def assets():
    
    screen.blit(road,(0,10))

while True:
    #clock.tick(60)
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    assets()
    pygame.display.update()
   



