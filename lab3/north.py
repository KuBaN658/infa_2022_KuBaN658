import pygame

pygame.init()

WIDTH = 800
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крайний север")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (211, 95, 95)
GREY = (230, 230, 230)
DARK_GREY = (204, 204, 204)
BLUE = (147, 172, 167)
DARK_BLUE = (0, 1, 252)
BEIGE = (227, 222, 219)
BROWN = (145, 124, 111)
DARK_BROWN = (108, 93, 83)
LIGHT_BROWN = (172, 157, 147)

FPS = 60
clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.draw.rect(screen, GREY, (0, 0, WIDTH, HEIGHT//2))


def jurt(width, coords):
    height = width // 2
    surf_jurt = pygame.Surface((width, height))
    surf_jurt.fill((0, 0, 1))

    pygame.draw.circle(surf_jurt, GREY, (height, height), height)
    pygame.draw.circle(surf_jurt, BLACK, (height, height), height, 2)
    surf_jurt.set_colorkey((0, 0, 1))

    interval = width // 7
    #h_rect = height * 0.25
    x = 0
    y = width//2 - 1
    h = 0
    w = width // 5
    pygame.draw.line(surf_jurt, BLACK, (x, y), (width - x, y))
    for i in range(3):
        y = y - interval
        h += interval
        x = height - (height ** 2 - h ** 2) ** 0.5
        pygame.draw.line(surf_jurt, BLACK, (x, y), (width - x, y))
        x1 = x + w//2
        y1 = y
        x2 = x + w//2
        y2 = y + interval
        while x1 < width - x:
            pygame.draw.line(surf_jurt, BLACK, (x1, y1), (x2, y2))
            x1 += w
            x2 += w

    pygame.draw.line(surf_jurt, BLACK, (height, y), (height, 0))

    return screen.blit(surf_jurt, coords)


def draw_ellipse(width, height, color):
    surf_ellipse = pygame.Surface((width, height))
    pygame.draw.ellipse(surf_ellipse, color, (0, 0, width, height))
    surf_ellipse.set_colorkey(BLACK)
    return surf_ellipse


def cat(width_cat, coords):
    torso = draw_ellipse(width_cat, width_cat//2, DARK_GREY)
    screen.blit(torso, coords)
    nail = draw_ellipse(width_cat, width_cat//3, DARK_GREY)
    nail = pygame.transform.rotate(nail, 45)
    screen.blit(nail, (coords[0] + width_cat//2.5, coords[1] - width_cat//2.6))
    leg = draw_ellipse(width_cat*0.7, width_cat*0.2, DARK_GREY)
    leg1 = pygame.transform.rotate(leg, -160)
    leg2 = pygame. transform.rotate(leg, -145)
    leg3 = pygame.transform.rotate(leg, -40)
    leg4 = pygame.transform.rotate(leg, -55)
    screen.blit(leg1, (width_cat*0.3, width_cat*2.5))
    screen.blit(leg2, (width_cat*0.8, width_cat*1.07))
    screen.blit(leg3, (width_cat*2.5, width_cat*1.04))
    screen.blit(leg4, (width_cat*2.5, width_cat*1.04))
    surf_fish = pygame.Surface((int(width_cat * 0.5), int(width_cat * 0.5)))
    surf_fish.fill(WHITE)
    surf_fin = pygame.Surface((width_cat*0.2, width_cat*0.2))
    surf_fin.fill(WHITE)
    pygame.draw.polygon(surf_fin, RED,
                        [[0, width_cat*0.14], [width_cat*0.07, width_cat*0.2], [width_cat*0.14, 0],
                         [width_cat*0.2, width_cat*0.07]])
    pygame.draw.polygon(surf_fin, BLACK,
                        [[0, width_cat * 0.14], [width_cat * 0.07, width_cat * 0.2], [width_cat * 0.14, 0],
                         [width_cat * 0.2, width_cat * 0.07]], 1)
    surf_fin = pygame.transform.rotate(surf_fin, 45)
    surf_fish.blit(surf_fin, (width_cat*0.075, width_cat*0.055))
    surf_torso_fish = pygame.Surface((int(width_cat*0.3), int(width_cat*0.3)))
    surf_torso_fish.fill(WHITE)
    pygame.draw.circle(surf_torso_fish, BLUE, (width_cat*0.15, -width_cat*0.255), width_cat*0.3)
    pygame.draw.circle(surf_torso_fish, BLACK, (width_cat * 0.15, -width_cat * 0.255), width_cat * 0.3, 1)
    surf_torso_fish.set_colorkey(WHITE)


    surf_torso_fish_up = pygame.transform.flip(surf_torso_fish, 0, 1)
    surf_fish.blit(surf_torso_fish,(width_cat*0.1, width_cat*0.2))
    surf_fish.blit(surf_torso_fish_up, (width_cat*0.1, -width_cat*0.1))
    surf_fish.set_colorkey(WHITE)
    pygame.draw.polygon(surf_fish, BLUE,
                        [[width_cat*0.4, width_cat*0.2], [width_cat*0.45, width_cat*0.25], [width_cat*0.45, width_cat*0.15]])
    pygame.draw.polygon(surf_fish, BLACK,
                        [[width_cat*0.4, width_cat*0.2], [width_cat * 0.45, width_cat*0.25],
                         [width_cat*0.45, width_cat*0.15]], 1)
    pygame.draw.circle(surf_fish, DARK_BLUE, (width_cat * 0.15, width_cat * 0.2), width_cat*0.015)
    surf_fish = pygame.transform.rotate(surf_fish, -45)

    surf_head_cat = pygame.Surface((width_cat*0.3, width_cat*0.3))
    surf_fish.blit(surf_head_cat, (width_cat*0.1, width_cat*0.1))
    screen.blit(surf_fish, (coords[0] * 0.5, coords[1] * 0.98))
    return screen



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    jurt(400, (50, 400))
    jurt(600, (10, 50))
    jurt(100, (600, 700))
    cat(300, (100, 700))
    #cat(200, (100, 200))
    pygame.display.update()

    clock.tick(FPS)