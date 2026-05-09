import pygame
import random
import time

clock = pygame.time.Clock()

enemy_speed = 5
last_spawn_time = time.time()

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
carrect1.x = 150
carrect1.y = 500

carrect2 = yellowcar.get_rect()
carrect2.x = 0
carrect2.y = 0

#alternate spawn locations


bgy1=0
bgy2 = -650



bgspeed = 2



def assets():
    
    screen.blit(scaledimage,(0,bgy1))
    screen.blit(scaledimage,(0,bgy2))
    screen.blit(scaledimage2,carrect1)
    screen.blit(scaledimage3,carrect2)

def spawn():
    global last_spawn_time
    carrect2.y += enemy_speed
    if carrect2.y > 650:
        if time.time()-last_spawn_time >=2:
            spawning = random.randint(1,3)
            if spawning == 1:
                carrect2.x = 150
                carrect2.y = 0  
            elif spawning == 2:
                carrect2.x = 50
                carrect2.y = 0 
            elif spawning == 3:
                carrect2.x = 200
                carrect2.y = 0 
            carrect2.y = -150
            last_spawn_time = time.time()  
    #screen.blit(scaledimage3,carrect2)
        

    
while True:
    clock.tick(120)
  
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and carrect1.x>90:
            carrect1.x-=7

        if keys[pygame.K_d] and carrect1.x<300:
            carrect1.x+=7



    bgy1+=bgspeed
    bgy2+=bgspeed
    if bgy1 >= 650:
        bgy1=bgy2-650
    if bgy2 >=610:
        bgy2=bgy1-650


    spawn()
    assets()
    pygame.display.update()
   





