import pygame

pygame.init()

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("События от клавиатуры")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

x = WIDTH//2
y = HEIGHT//2
speed = 5


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)
