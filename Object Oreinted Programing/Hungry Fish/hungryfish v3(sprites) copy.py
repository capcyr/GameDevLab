import pygame
import random
import time

pygame.init()

width = 900
height = 825

score = 0

screen = pygame.display.set_mode((width,height))
screen.fill("white")
#Fonts
scorefont = pygame.font.SysFont("Calibri",size = 30)

gameover = pygame.font.SysFont("Calibri",size = 80)

#scaled images
fish = pygame.image.load("./sprites/fish.png")
scaledfish = pygame.transform.scale(fish,(50,37.5))

seabackground = pygame.image.load("./sprites/seabg.jpg")
scaledbg = pygame.transform.scale(seabackground,(825,900))

sharky = pygame.image.load("./sprites/shark.png")
scaledshark = pygame.transform.scale(sharky,(60,40))

class Fishsprite(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
#superfunction is used to access properties of parent class
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(50,760)
        self.rect.y = random.randrange(50,850)


class Sharksprite(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(50,760)
        self.rect.y = random.randrange(50,850)




blockgroup = pygame.sprite.Group()
allspritelist = pygame.sprite.Group()








for i in range(60):
    food = Fishsprite(scaledfish)
    
    blockgroup.add(food)
    allspritelist.add(food)
#adds food to all sprite and block groups
sharking = Sharksprite(scaledshark)
allspritelist.add(sharking)

sharking.rect.x = 250
sharking.rect.y = 250

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.blit(seabackground,(0,0))

    scoretext = scorefont.render(f"Score:{score}",True,"black")
    gameovertext = gameover.render("Game Over", True, "Red")

    screen.blit(scoretext, (50,0))

    pos = pygame.mouse.get_pos()
    sharking.rect.x = pos[0]
    sharking.rect.y = pos[1]

    blockhitlist= pygame.sprite.spritecollide(sharking,blockgroup,True)
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

