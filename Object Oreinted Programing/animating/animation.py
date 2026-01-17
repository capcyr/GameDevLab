import pygame

pygame.init()

screen = pygame.display.set_mode((800,750))
pygame.display.set_caption("Happy Birthday whoever")
birthday = pygame.image.load("birthday.jpg")
christmas = pygame.image.load("christmas.jpg")
easter = pygame.image.load("easter.jpg")
halloween = pygame.image.load("halloween.jpg")

#resizing the images
birthday = pygame.transform.scale(birthday,(800,750))
christmas = pygame.transform.scale(christmas,(800,750))
easter = pygame.transform.scale(easter,(800,750))
halloween = pygame.transform.scale(halloween,(800,750))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    font1 = pygame.font.SysFont("comicsans",45)
    font2 = pygame.font.SysFont("Italic",65)
    font3 = pygame.font.SysFont("TimesNewRoman",55)
    font4 = pygame.font.SysFont("Aptos",55)
    screen.blit(birthday,(0,0))
    text = font1.render("Happy",True,"black")
    text2 = font1.render("Birthday",True,"black")
    #blitting
    screen.blit(text,(320,350))
    screen.blit(text2,(320,410))
    pygame.display.update()
    #image2
    pygame.time.delay(2000)
    screen.blit(christmas,(0,0))
    text3 = font2.render("Merry",True,"black")
    text4 = font2.render("Christmas",True,"black")
    screen.blit(text3,(250,380))
    screen.blit(text4,(250,430))
    pygame.display.update()
    pygame.time.delay(2000)
    screen.blit(easter,(0,0))
    text5 = font3.render("Happy",True,"black")
    text6 = font3.render("Easter",True,"black")
    screen.blit(text5,(250,150))
    screen.blit(text6,(250,210))



    pygame.display.update()
    pygame.time.delay(2000)
    pygame.time.delay(2000)
pygame.quit()

