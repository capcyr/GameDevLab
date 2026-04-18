from pygame.locals import*
import pygame

pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000,750))
run = True
clock=pygame.time.Clock()

background = pygame.image.load("spacebg.jpg")
#fontstyles
healthfont = pygame.font.SysFont("Times New Roman",size = 50)
winfont  = pygame.font.SysFont("Times New Roman",size = 60)

#gaming variables

blueplayerhealth = 5
redplayerhealth = 5

gameover = False

bulletspeed = 6

fps = 60

maxbullets = 4
spaceshipwidth,spaceshipheight = 100,100
#loading spaceship images
bluespaceship = pygame.image.load("spaceship2.png")
greyspaceship = pygame.image.load("spaceship1.png")

border = pygame.Rect(500,0,10,750)
bluebullets = []
greybullets = []

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
         if self.rect.top <= 0 or self.rect.bottom >= 750:
              self.rect.move_ip(0, -velocity)

#CREATING OBJECT
player1blue = spaceship(bluespaceship,0,375)
player2grey = spaceship(greyspaceship,900,375)
sprites = pygame.sprite.Group()
sprites.add(player1blue)
sprites.add(player2grey)

def drawhealth():
     bluetext = healthfont.render("BlueHealth "+str(blueplayerhealth),True,"Blue")
     redtext = healthfont.render("RedHealth "+str(redplayerhealth),True,"Red")
     screen.blit(bluetext,(10,20))
     screen.blit(redtext,(720,20))

def gamewin():
     global gameover
     gamewinp1 = healthfont.render("Game Won By Player 1 ",True,"Blue")
     gamewinp2 = healthfont.render("Game Won By Player 2 ",True,"Red")
     if blueplayerhealth <= 0:
          screen.fill("black")
          screen.blit(gamewinp2,(320,350))
          gameover = True
     if redplayerhealth <= 0:
          screen.fill("black")
          screen.blit(gamewinp1,(320,350))
          gameover = True
     

while run:
    clock.tick(60)
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                run = False

         if event.type == pygame.KEYDOWN:
               if event.key == K_f and len(bluebullets)<maxbullets:
                    bullet = pygame.Rect(player1blue.rect.right,
                                   player1blue.rect.y+player1blue.rect.height//2,
                                   10,5)
                    bluebullets.append(bullet)

               if event.key == K_h and len(greybullets)<maxbullets:
                    bullet = pygame.Rect(player2grey.rect.right,
                                   player2grey.rect.y+player2grey.rect.height//2,
                                   10,5)
                    greybullets.append(bullet)
    KEY = pygame.key.get_pressed()
    if KEY[K_a]:
         player1blue.moveleftright(-4,1)
    if KEY[K_d]:
         player1blue.moveleftright(4,1)
    if KEY[K_w]:
         player1blue.moveupdown(-4)
    if KEY[K_s]:
         player1blue.moveupdown(4)

    if KEY[K_LEFT]:
         player2grey.moveleftright(-4,2)
    if KEY[K_RIGHT]:
         player2grey.moveleftright(4,2)
    if KEY[K_UP]:
         player2grey.moveupdown(-4)
    if KEY[K_DOWN]:
         player2grey.moveupdown(4)
     
    
    for bullet in bluebullets:
         bullet.x+=bulletspeed

         if player2grey.rect.colliderect(bullet):
              redplayerhealth-=1
              bluebullets.remove(bullet) 
         if bullet.x > 1000:
              bluebullets.remove(bullet)

    for bullet in greybullets:
         bullet.x-=bulletspeed

         if player1blue.rect.colliderect(bullet):
              blueplayerhealth-=1
              greybullets.remove(bullet) 
         if bullet.x < 0:
              greybullets.remove(bullet)
         

    
    screen.blit(background,(0,0))
    if not gameover:
         sprites.draw(screen)
         for bullet in bluebullets:
          pygame.draw.rect(screen,(0,0,255),bullet) 

         for bullet in greybullets:
          pygame.draw.rect(screen,(255,0,0),bullet) 
    drawhealth()
    gamewin()
     


    

    pygame.display.update()
pygame.quit()
