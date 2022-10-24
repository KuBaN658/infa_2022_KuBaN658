import pygame
from pygame.draw import *

pygame.init()

FPS = 30
grey = (192, 192, 192)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
size = 250
screen = pygame.display.set_mode((size*4, size*4))
rect(screen, grey, (0, 0, size*4, size*4))
circle(screen, yellow, (size*2, size*2), size)
circle(screen, black, (size*2, size*2), size, 2)
rect(screen, black, (2*size - 0.5*size, 2*size + 0.5*size, size, size//5))
def caunt_coords_polygon():


#polygon(screen, black, [size, size])




pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()