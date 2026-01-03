import pygame
import random
pygame.init()
screening = pygame.display.set_mode((800,750))
screening.fill("black")
#class for the circle
class circular:
    def __init__(self,color,position,radius,width =0):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width
        self.screen = screening
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.radius,self.width)
    #function for growing the circle
    def grow(self,x):
        self.radius+=x
        self.draw()

    def shrink(self,x):
        self.radius=max(1,self.radius-x)
        self.draw()

    def colors(self):
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.draw()







#creating objects
circle1 = circular("blue",(420,380),80)
circle2 = circular("red",(420,380),60)
circle3 = circular("green",(420,380),50)
circle4 = circular("Yellow",(420,380),40)
#reset()
circles = [circle1,circle2,circle3,circle4]

def reset():
    global circles
    screening.fill("Black")
    for c in circles:
        c.draw()
    pygame.display.update()

    
run = True
while run:
    pygame.display.update()
#quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.MOUSEBUTTONUP:
            for c in circles:
                c.grow(4)
            pygame.display.update

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                for c in circles:
                    c.shrink(2)

            elif event.key == pygame.K_r:
                reset()
            pygame.display.update
pygame.quit()

