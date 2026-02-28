import pygame
import time
import random
from pygame.locals import*

pygame.init()
pygame.display.set_caption("Recycle this")
screen = pygame.display.set_mode((1000,750))
run = True 

scoringfont = pygame.font.SysFont("Calibri",size = 50)
t = time.time()








background = pygame.image.load("leaves.jpg")
box = pygame.image.load("box.png")
coke = pygame.image.load("coke.png")
pencil = pygame.image.load("pencil.png")
plastic = pygame.image.load("plastic.png")
recycling = pygame.image.load("recycling.png")
recyclables = ["coke.png","box.png","pencil.png"]
scoring = 0

text = scoringfont.render("score:",str(scoring),True,"Red")
#Recycle bin class
class recyclebin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = recycling
        self.image = pygame.transform.scale(self.image,(133,200))
        self.rect = self.image.get_rect()
#unrecyclable
class plasticbag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = plastic
        self.image = pygame.transform.scale(self.image,(75,100))
        self.rect = self.image.get_rect()

class recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(75,100))
        self.rect = self.image.get_rect()


bin = recyclebin()
spritegroup = pygame.sprite.Group()
nonrecyclable = pygame.sprite.Group()
spritegroup.add(bin)
recyclegroup = pygame.sprite.Group()
nonrecyclegroup = pygame.sprite.Group()

#creating plastic bags
for i in range(11):
    bag =  plasticbag()
    nonrecyclable.add(bag)
    bag.rect.x = random.randint(10,1000)
    bag.rect.y = random.randint(10,700)
    spritegroup.add(bag)
    nonrecyclegroup.add(bag)
#Non recyclable items
for i in range(11):
    rec = recyclable(random.choice(recyclables))
    recyclegroup.add(rec)
    rec.rect.x = random.randint(10,1000)
    rec.rect.y = random.randint(10,700)
    spritegroup.add(rec)
    

while run:
    elasped = time.time()-t
    if elasped > 60:
        if scoring >5:
            text = scoringfont.render("You Win",True,"Red") 
        else:
            text = scoringfont.render("You Lose",True,"Red") 
        screen.blit(text,(450,365))
        pygame.display.update() 

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keystore = pygame.key.get_pressed()
        if keystore[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y-=0.6
        if keystore[pygame.K_DOWN]:
            if bin.rect.y < 600:
                bin.rect.y+=0.5
        if keystore[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x-=0.6
        if keystore[pygame.K_RIGHT]:
            if bin.rect.x < 880:
                bin.rect.x+=0.6
        #Collision between items
        hitrecycle = pygame.sprite.spritecollide(bin,recyclegroup,True)
        nonrec = pygame.sprite.spritecollide(bin,nonrecyclegroup,True)
        for i in hitrecycle:
            scoring+=1
            text = scoringfont.render("score:"+str(scoring),True,"Red")
        for i in nonrec:
            scoring-=1
            text = scoringfont.render("score:"+str(scoring),True,"Red")




        screen.blit(background,(0,0))
        screen.blit(text,(800,0))
        spritegroup.draw(screen)
        timingfont = scoringfont.render("Time Left"+str(60-int(elasped)),True,"red")
        screen.blit(timingfont,(10,0))
    pygame.display.update()
        
pygame.quit()












