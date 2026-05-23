import pygame
import time
import random
pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 936 
groundscroll = 0
groundspeed = 4

flying = False

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")

bg = pygame.image.load("images/bg.png")
ground = pygame.image.load("images/ground.png")
pipes = pygame.image.load("images/pipes.png")
restart = pygame.image.load("images/restart.png")

def display():
    screen.blit(ground,(groundscroll,766))
class Birb(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f'images/birb{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False
    def update(self):
        if flying == True:
            self.vel +=0.5
            if self.rect.bottom < 768:
                self.rect.y += self.vel
            if self.vel > 8:
                self.vel = 8
        
            
        if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
            self.clicked = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked = False
        self.counter+=1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.images[self.index],self.vel*-2)
    


bird_group = pygame.sprite.Group()
flappy = Birb(100,int(screen_height/2))
bird_group.add(flappy)






run = True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    bird_group.draw(screen)
    bird_group.update()
    display()
    groundscroll-=groundspeed
    if groundscroll>35:
        groundscroll = 0
        


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False:
            flying = True 
    pygame.display.update()
pygame.quit()
