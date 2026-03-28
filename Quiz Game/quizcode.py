from pygame.locals import*
import pygame
pygame.font.init()
pygame.mixer.init()


screen = pygame.display.set_mode((1000,750))
run = True


background = pygame.image.load("spacebg.jpg")
#fontstyles
healthfont = pygame.font.SysFont("Times New Roman",size = 50)
winfont  = pygame.font.SysFont("Times New Roman",size = 60)

#gaming variables

blueplayerhealth = 5
redplayerhealth = 5

bulletspeed = 6

fps = 60

maxbullets = 4
spaceshipwidth,spaceshipheight = 100,100
#loading spaceship images
bluespaceship = pygame.image.load("spaceship2.png")
greyspaceship = pygame.image.load("spaceship1.png")

border = pygame.Rect(500,0,10,750)

#class for spaceship
class spaceship(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = pygame.transform.scale(image,(spaceshipwidth,spaceshipheight))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
    #horizontal movement
    def moveleftright(self,velocity,player):
        self.rect.x+= velocity
        if player ==1:
             if self.rect.left<=0 or self.rect.right>=border.left:
                  self.rect.move_ip(-velocity,0)
        if player ==2:
             if self.rect.left <=border.right or self.rect.right >= 1000:
                  self.rect.move_ip(-velocity,0)
    #vertical movement 
    def moveupdown(self,velocity):
         self.rect.move_ip(0,velocity)
         if self.rect.top <= 0 or self.rect.bottom >= 1000:
              self.rect.move_ip(0, -velocity)







#CREATING OBJECT
player1blue = spaceship(bluespaceship,0,375)
player2grey = spaceship(greyspaceship,900,375)
sprites = pygame.sprite.Group()
sprites.add(player1blue)
sprites.add(player2grey)




while run:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                run = False
    KEY = pygame.key.get_pressed()
    if KEY[K_a]:
         player1blue.moveleftright(-2,1)
    if KEY[K_d]:
         player1blue.moveleftright(2,1)
    if KEY[K_w]:
         player1blue.moveupdown(-2)
    if KEY[K_s]:
         player1blue.moveupdown(2)

    if KEY[K_LEFT]:
         player2grey.moveleftright(-2,1)
    if KEY[K_RIGHT]:
         player2grey.moveleftright(2,1)
    if KEY[K_UP]:
         player2grey.moveupdown(-2)
    if KEY[K_DOWN]:
         player2grey.moveupdown(2)

    
    screen.blit(background,(0,0))
    sprites.draw(screen)



    pygame.display.update()
pygame.quit()



