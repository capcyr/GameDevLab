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
pipe_gap = 150
pipefrequency = 1500
score = 0
font = pygame.font.SysFont("Bauhaus 93",60)
lastpipe = pygame.time.get_ticks()-pipefrequency
passpipe = False
gameover = False


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
    
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x,y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/pipes.png")
        self.rect = self.image.get_rect()
        if position ==1:
            self.image = pygame.transform.flip(self.image, False,True)
            self.rect.bottomleft = [x,y-int(pipe_gap/2)]
        if position ==-1:
            self.rect.topleft = [x,y + int(pipe_gap/2)]
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

def draw(text, font, text_col, x,y):
    img = font.render(text,True, text_col)
    screen.blit(img,(x,y))

def resetgame():
    global score
    global gameover, flying, ground, groundscroll, pipefrequency, lastpipe,groundspeed,currenttime
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height/2)
    flappy.vel = 0
    flappy.index = 0
    flappy.image = flappy.images[0]
    score = 0
    gameover = False
    flying = False
    groundspeed = 0
    groundscroll = 0
    lastpipe = pygame.time.get_ticks()-pipefrequency
    pipefrequency = 1500
    return score

class Button():
    def __init__(self, x,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action = True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action




buttoning = Button(screen_width/2-50,screen_height/2-100,restart)
pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
flappy = Birb(100,int(screen_height/2))
bird_group.add(flappy)






run = True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    display()
    groundscroll-=groundspeed
    if abs(groundscroll)>35:
        groundscroll = 0
    if len(pipe_group)>0:
        if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.left\
        and bird_group.sprites()[0].rect.right<pipe_group.sprites()[0].rect.right\
        and passpipe == False:
            passpipe = True
    if passpipe == True:
        if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.right:
            score+=1
            passpipe = False
    draw(str(score),font, "white",int(screen_width/2),20)

    currenttime = pygame.time.get_ticks()
    if not gameover and currenttime-lastpipe>pipefrequency:
        pipeheight = random.randint(-100,100)
        piping = Pipe(screen_width,int(screen_height/2)+pipeheight,-1)
        toppipe = Pipe(screen_width,int(screen_height/2)+pipeheight,1)
        pipe_group.add(piping)
        pipe_group.add(toppipe)
        lastpipe = currenttime
        
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        gameover = True

    if gameover:
        groundspeed = 0
        if buttoning.draw():
            resetgame()
        
        
        
    if not gameover:  
        pipe_group.update()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False:
            flying = True 
    pygame.display.update()
pygame.quit()
