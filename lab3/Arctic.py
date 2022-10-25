import pygame
from pygame.draw import *

pygame.init()

FPS = 30
grey = (230, 230, 230)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (145, 124, 111)
dark_brown = (108, 93, 83)
blue = (147, 172, 167)
red = (192, 90, 90)
dark_blue = (22, 26, 242)
screen = pygame.display.set_mode((850, 1000))
rect(screen, grey, (0, 0, 850, 500), 0)
rect(screen, white, (0, 500, 850, 500), 0)
circle(screen, black, (300, 600), 150, 3)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()