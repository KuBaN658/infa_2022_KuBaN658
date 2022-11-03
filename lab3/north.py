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


def jurt(width_jurt, coords):
    height_jurt = width_jurt//2
    surf_jurt = pygame.Surface((width_jurt, height_jurt))

    surf_jurt.fill((0, 0, 1))
    pygame.draw.circle(surf_jurt, GREY, (height_jurt, height_jurt*1.25), height_jurt)
    pygame.draw.circle(surf_jurt, BLACK, (height_jurt, height_jurt*1.25), height_jurt, 2)
    surf_jurt.set_colorkey((0, 0, 1))

    h = width_jurt//2//3.5
    h_rect = height_jurt*0.25
    y = height_jurt - 1
    w = width_jurt//5

    for i in range(3):
        cath = (height_jurt**2 - h_rect**2)**0.5
        x = height_jurt - cath

        pygame.draw.line(surf_jurt, BLACK, (x, y), (width_jurt - x, y))

        y -= h
        h_rect += h
        abcissa = x + width_jurt//30

        while abcissa < cath*2 + x:
            pygame.draw.line(surf_jurt, BLACK, (abcissa, y), (abcissa, y + h))
            abcissa += w

    surf_jurt_upper = pygame.Surface((width_jurt, height_jurt))
    surf_jurt_upper.fill(GREY)
    pygame.draw.rect(surf_jurt_upper, (255, 255, 254), (0, height_jurt//2, width_jurt, height_jurt//2))
    pygame.draw.circle(surf_jurt_upper, WHITE, (height_jurt, height_jurt * 1.25), height_jurt)
    surf_jurt_upper.set_colorkey(WHITE)
    surf_jurt.blit(surf_jurt_upper, (0, 0))

    return screen.blit(surf_jurt, coords)


def draw_ellipse(width_ellipse, color):
    surf_ellipse = pygame.Surface((width_ellipse, width_ellipse//2))
    pygame.draw.ellipse(surf_ellipse, color, (width_ellipse//4, width_ellipse//4, width_ellipse//2, width_ellipse//8))
    surf_ellipse.set_colorkey(BLACK)
    return surf_ellipse


def cat(width_cat, coords):
    torso = draw_ellipse(width_cat, DARK_GREY)
    return screen.blit(torso, coords)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    jurt(400, (50, 400))
    cat(300, (100, 700))
    pygame.display.update()

    clock.tick(FPS)