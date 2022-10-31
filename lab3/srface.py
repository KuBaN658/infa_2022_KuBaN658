import pygame

pygame.init()

WIDTH = 1900
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Класс Surface")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

surf = pygame.Surface((WIDTH, 200)) #создаем поверхность
bita = pygame.Surface((50, 10))

surf.fill(BLUE)
bita.fill(RED)

b_x, b_y = 0, 100
x, y = 0, 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.fill(BLUE)
    surf.blit(bita,(b_x, b_y))
    if b_x < WIDTH:
        b_x += 5
    else:
        b_x = 0
    if y < HEIGHT:
        y += 1
    else:
        y = 0

    screen.fill(WHITE)
    surf.set_alpha(255)  #Задает прозрачность поверхности 0 - 255
    screen.blit(surf, (x, y))  # накладывает поверхность
    pygame.display.update()

    clock.tick(FPS)
