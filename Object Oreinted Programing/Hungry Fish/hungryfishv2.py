import pygame
import random
import time

pygame.init()

width = 825
height = 900

score = 0

screen = pygame.display.set_mode((height,width))
screen.fill("white")

scorefont = pygame.font.SysFont("Calibri",size = 30)

gameover = pygame.font.SysFont("Calibri",size = 80)

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
    food.rect.x = random.randrange(50,760)
    food.rect.y = random.randrange(50,850)
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

    scoretext = scorefont.render(f"Score:{score}",True,"black")
    gameovertext = gameover.render("Game Over", True, "Red")

    screen.blit(scoretext, (0,0))

    pos = pygame.mouse.get_pos()
    fish.rect.x = pos[0]
    fish.rect.y = pos[1]

    blockhitlist= pygame.sprite.spritecollide(fish,blockgroup,True)
    if blockhitlist:
        score+=1

    if score == 50:
        screen.fill("black")
        screen.blit(gameovertext, (300, 450))
        pygame.display.flip()  # Shows the text on screen
        pygame.time.delay(5000)  # Pauses for 5000 milliseconds (5 seconds)
        run = False

        



    allspritelist.draw(screen)

    pygame.display.update()

