import pygame
import time
import random
pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")

bg = pygame.image.load("images/bg.png")
ground = pygame.image.load("images/ground.png")
pipes = pygame.image.load("images/pipes.png")
restart = pygame.image.load("images/restart.png")


def display():
    screen.blit(ground,(0,766))


run = True
while run:
    screen.blit(bg,(0,0))
    display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()