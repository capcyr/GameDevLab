import pygame
import math
import time


clock = pygame.time.Clock()

maze = [
    "11111111111111111111",
    "10000000001100000001",
    "10111111101101111101",
    "10100000100000000101",
    "10101110111110110101",
    "10001000001000001001",
    "11101111101111101111",
    "10000000100000000001",
    "10111110111110111101",
    "10000000000000000001",
    "11111111111111111111",
]


pygame.init()

width = 550
height = 625

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pacman")


tile = 28

x,y = 1*tile,1*tile


#placeholder value
x = 400
y = 400

speed = 3

direction = ("RIGHT")

mouthangle = 0

opening = True

run = True

def draw_pacman(x, y, centerangle):
    start_angle = math.radians(centerangle-22.5)
    end_angle = math.radians(centerangle+22.5)
    pygame.draw.circle(screen, "#FFFF00", (x, y), 12)
    pygame.draw.polygon(screen, "#000000", [
        (x, y),
        (x + 20 * math.cos(start_angle), y - 20 * math.sin(start_angle)),
        (x + 20 * math.cos(end_angle), y - 20 * math.sin(end_angle))
    ])


def draw_maze():
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column]=="1":
                pygame.draw.rect(screen,"#0400FF",(column*tile,row*tile,tile,tile))






while run:
    screen.fill("black")
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False



    draw_maze()
    draw_pacman(x,y,0)




    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        draw_pacman(x,y,180)
       
    elif keys[pygame.K_RIGHT]:
        draw_pacman(x,y,0)

    elif keys[pygame.K_UP]:
        draw_pacman(x,y,90)
        

    elif keys[pygame.K_DOWN]:
        draw_pacman(x,y,270)
        



    pygame.display.update()