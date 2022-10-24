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


def caunt_point_polygon(x0, y0, x1, y1, width):
    hypotenuse = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    x = abs(y1 - y0) / hypotenuse * width
    y = abs(x1 - x0) / hypotenuse * width
    x_point = x0 + x
    if y0 < y1:
        y_point = y0 - y
    else:
        y_point = y0 + y
    coords_second = x_point, y_point
    x_point = x1 + x
    if y0 < y1:
        y_point = y1 - y
    else:
        y_point = y1 + y
    coords_first = x_point, y_point
    coords = [coords_first, coords_second]
    coords = [(x0, y0), (x1, y1)] + coords
    print(coords)
    return coords


polygon(screen, black, caunt_point_polygon(size, size + size/5, 2*size - size/5, 2*size - size/2 + size/5, 25))
polygon(screen, black, caunt_point_polygon(size*2 + size/5, 2*size - size/2.6, size*3, size+size/3, 25))
circle(screen, red, (size + size/2, size + size/1.33), size/5)
circle(screen, black, (size + size/2, size + size/1.33), size/5, 2)
circle(screen, black, (size + size/2, size + size/1.33), size/13)
circle(screen, red, (2*size + size/2, size + size/1.33), size/8)
circle(screen, black, (2*size + size/2, size + size/1.33), size/8, 2)
circle(screen, black, (2*size + size/2, size + size/1.33), size/15)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
