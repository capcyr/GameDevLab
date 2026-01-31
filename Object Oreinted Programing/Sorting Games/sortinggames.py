import pygame


pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill("Black")

pygame.display.update()

brawlstars = pygame.image.load("brawlstars.png")
candycrush = pygame.image.load("candycrush.jpg")
roblox = pygame.image.load("roblox.png")
subway = pygame.image.load("subway.jpg")

#Blitting images on the screen
screen.blit(brawlstars,(170,800))
screen.blit(candycrush,(170,550))
screen.blit(roblox,(170,280))
screen.blit(subway,(170,30))
pygame.display.update()
font = pygame.font.SysFont("calibri",50)

text1 = font.render("Roblox",True,"Red")
screen.blit(text1,(700,800))
text2 = font.render("Candycrush",True,"Red")
screen.blit(text2,(700,550))
text3 = font.render("Subway",True,"Red")
screen.blit(text3,(700,280))
text4 = font.render("Brawlstars",True,"Red")
screen.blit(text4,(700,30))
pygame.display.update()


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousepos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,"red",(mousepos),20,0)
        pygame.display.update()
