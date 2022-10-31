import pygame

pygame.init()

WIDTH = 1900
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

ground = HEIGHT - 70
jump_force = 40 # сила прыжка
move = jump_force + 1

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=WIDTH//2)
rect.bottom = ground

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force
    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force + 1

    screen.fill(WHITE)
    screen.blit(hero, rect)
    pygame.display.update()

    clock.tick(FPS)