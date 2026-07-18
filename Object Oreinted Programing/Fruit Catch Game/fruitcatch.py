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
ranfruit = 0
scaledimage = pygame.transform.scale(background,(1000,750))

scaledimage2 = pygame.transform.scale(apple,(100,106.944444444))
scaledimage3 = pygame.transform.scale(lemon,(100,100))
scaledimage4 = pygame.transform.scale(orange,(100,96.653543307))
scaledimage5 = pygame.transform.scale(watermelon,(100,80))

basketimage = pygame.transform.scale(basket,(150,90))
fruitlist = [scaledimage2, scaledimage3,scaledimage4, scaledimage5]
fruitchoose = random.choice(fruitlist)
fruit_x = random.randint(50,900)
fruit_y = -100
fruitspeed = 5

basketimage_x = 500
basketimage_y = 650






clock = pygame.time.Clock()

while run:
    clock.tick(120)

    
    screen.blit(scaledimage,(0,0))

    screen.blit(basketimage,(basketimage_x,basketimage_y))
    
    fruit_y +=fruitspeed
    screen.blit(fruitchoose,(fruit_x,fruit_y))


    if fruit_y > 750:
        fruitchoose = random.choice(fruitlist)
        fruit_x = random.randint(50,900)
        fruit_y = -100
        

        

    fruit_rect = fruitchoose.get_rect(topleft = (fruit_x,fruit_y))
    basketrect = basketimage.get_rect(topleft = (basketimage_x,basketimage_y))


    if fruit_rect.colliderect(basketrect):
        fruitchoose = random.choice(fruitlist)
        fruit_x = random.randint(50,900)
        fruit_y = -100
        scoring+=1


    scoretext = scoringfont.render(f"Score:{scoring}",True,"white")
    screen.blit(scoretext, (50,20))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and basketimage_x>50:
        basketimage_x-=15

    if keys[pygame.K_d] and basketimage_x<825:
        basketimage_x+=15


        
    

    pygame.display.update()
pygame.quit()
