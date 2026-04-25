import pygame
import random
import time

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((500,650))
pygame.display.set_caption("Car Game")

road = pygame.image.load("./images/road.jpg")
scaledimage = pygame.transform.scale(road,(500,650))


redcar = pygame.image.load("./images/redcar.png")
yellowcar = pygame.image.load("./images/yellowcar.png")

scaledimage2 = pygame.transform.rotate(pygame.transform.scale(redcar,(155,155)),(180))
scaledimage3 = pygame.transform.rotate(pygame.transform.scale(yellowcar,(75,150)),(180))


carrect1 = redcar.get_rect()
carrect1.x = 0
carrect1.y = 0

carrect2 = yellowcar.get_rect()
carrect2.x = 0
carrect2.y = 0

bgy1=0
bgy2 = -650



bgspeed = 2



def assets():
    
    screen.blit(scaledimage,(0,bgy1))
    screen.blit(scaledimage,(0,bgy2))
    screen.blit(scaledimage2,(200,500),carrect1)
    screen.blit(scaledimage3,carrect2)

    

while True:
    clock.tick(120)
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    bgy1+=bgspeed
    bgy2+=bgspeed
    if bgy1 >= 610:
        bgy1-=700
    if bgy2 >=610:
        bgy2-=700

    assets()
    pygame.display.update()
   



