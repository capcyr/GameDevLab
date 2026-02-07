import pygame
import time
import random
from pygame.locals import*

pygame.init()
pygame.display.set_caption("Recycle this")
screen = pygame.display.set_mode((1000,750))
run = True 


background = pygame.image.load("leaves.jpg")
box = pygame.image.load("box.png")
coke = pygame.image.load("coke.png")
pencil = pygame.image.load("pencil.png")
plastic = pygame.image.load("plastic.png")
recycling = pygame.image.load("recycling.png")

#Recycle bin class
class recyclebin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = recycling
        self.image = pygame.transform.scale(self.image,(133,200))
        self.rect = self.image.get_rect()
bin = recyclebin()
spritegroup = pygame.sprite.Group()
spritegroup.add(bin)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keystore = pygame.key.get_pressed()
    if keystore[pygame.K_UP]:
        if bin.rect.y > 0:
            bin.rect.y-=1
    if keystore[pygame.K_DOWN]:
        if bin.rect.y < 1000:
            bin.rect.y+=0.5
    screen.blit(background,(0,0))
    spritegroup.draw(screen)
    pygame.display.update()
        
pygame.quit()






