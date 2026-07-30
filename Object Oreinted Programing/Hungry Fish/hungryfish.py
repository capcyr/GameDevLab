import pygame
import random

pygame.init()

width = 825
height = 900

screen = pygame.display.set_mode((height,width))
screen.fill("white")


class Block(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
#superfunction is used to access properties of parent class
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

blockgroup = pygame.sprite.Group()
allspritelist = pygame.sprite.Group()



for i in range(60):
    food = Block("red", 20,15)
    food.rect.x = random.randrange(width)
    food.rect.y = random.randrange(height)
    blockgroup.add(food)
    allspritelist.add(food)
#adds food to all sprite and block groups
fish = Block("blue", 30,20)
allspritelist.add(fish)

fish.rect.x = 250
fish.rect.y = 250

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("white")

    pos = pygame.mouse.get_pos()
    fish.rect.x = pos[0]
    fish.rect.y = pos[1]

    blockhitlist= pygame.sprite.spritecollide(fish,blockgroup,True)


    allspritelist.draw(screen)

    pygame.display.update()

