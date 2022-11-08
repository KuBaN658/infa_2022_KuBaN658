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
TEMP_COLOR = (0, 0, 1)
FPS = 60
clock = pygame.time.Clock()


def draw_background(surface, color_sky, color_ground):
    '''
    Рисует фон изображения на экране.
    :param color_sky: цвет неба
    :param color_ground: цвет земли
    :param surface: поверхность
    :return: None
    '''
    surface.fill(color_ground)
    pygame.draw.rect(surface, color_sky, (0, 0, WIDTH, HEIGHT // 2))


def igloo(width, height, coords, color):
    '''
    рисует иглу
    :param width: Ширина иглу по нижнему краю
    :param height: высота иглу
    :param coords: координаты середины основания(кортеж(x, y))
    :param color: цвет иглы
    :return: None
    '''
    surf_jurt = draw_contour(width, height, color)


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
        x = height - (height ** 2 - h ** 2) ** 0.5 + 1
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

    screen.blit(surf_jurt, coords)


def draw_contour(width, height, color):
    surf_jurt = pygame.Surface((width, height))
    surf_jurt.fill(TEMP_COLOR)
    pygame.draw.circle(surf_jurt, color, (height, height), height)
    pygame.draw.circle(surf_jurt, BLACK, (height, height), height, 2)
    surf_jurt.set_colorkey(TEMP_COLOR)
    return surf_jurt


def draw_ellipse(width, height, color):
    surf_ellipse = pygame.Surface((width, height))
    pygame.draw.ellipse(surf_ellipse, color, (0, 0, width, height))
    surf_ellipse.set_colorkey(BLACK)
    return surf_ellipse


def chukchi(height, coords):
    width = height//1.5
    surf_chukchi = pygame.Surface((width, height))
    pygame.draw.ellipse(surf_chukchi, BEIGE, (width*0.22, 0, width*0.5, width*0.4))
    torso = pygame.Surface((width//1.3, width*0.8))
    pygame.draw.ellipse(torso, BROWN, (0, 0, width//1.3, width*2))
    torso.set_colorkey(BLACK)

    surf_chukchi.blit(torso, (width*0.095,  width*0.18))
    pygame.draw.ellipse(surf_chukchi, (172, 157, 147),
                        (width * 0.27, width * 0.06, width * 0.4, width * 0.3))
    pygame.draw.ellipse(surf_chukchi, BEIGE, (width*0.32, width*0.1, width*0.3, width*0.2))
    hand = draw_ellipse(width//3, width//10, BROWN)
    surf_chukchi.blit(hand, (0, width//2.5))
    hand_left = pygame.transform.rotate(hand, 150)
    surf_chukchi.blit(hand_left, (width//1.7, width//2.9))
    leg = draw_ellipse(width//6, width//3, BROWN)
    surf_chukchi.blit(leg, (width//4, width*0.825))
    surf_chukchi.blit(leg, (width//1.8, width*0.825))
    foot = draw_ellipse(width//4, width//8, BROWN)
    surf_chukchi.blit(foot, (width//6, height*0.7))
    surf_chukchi.blit(foot, (width//1.8, height*0.7))
    pygame.draw.line(surf_chukchi, (0, 0, 1), (width*0.03, 0), (width*0.08, height*0.7))
    pygame.draw.line(surf_chukchi, (0, 0, 1), (width*0.37, width*0.15), (width*0.43, width*0.17))
    pygame.draw.line(surf_chukchi, (0, 0, 1), (width*0.5, width*0.17), (width*0.56, width*0.15))
    pi = 3.14
    pygame.draw.arc(surf_chukchi, (0, 0, 1), (width*0.42, width*0.22, width*0.1, width*0.05), 0, pi)
    pygame.draw.rect(surf_chukchi, DARK_BROWN, (width*0.1, width*0.88, width*0.76, width*0.1))
    pygame.draw.rect(surf_chukchi, DARK_BROWN, (width*0.38, width*0.35, width*0.2, width*0.6))

    surf_chukchi.set_colorkey(BLACK)
    return screen.blit(surf_chukchi, coords)


def draw_fish(width):
    surf_fish = pygame.Surface((width*1.5, width*1.5))
    surf_fin = pygame.Surface((width//2, width//2))
    pygame.draw.polygon(surf_fin, RED, [[0, width//3], [width//2, width//6],
                                        [width//3, 0], [width//6, width//2]])
    pygame.draw.polygon(surf_fin, (0, 0, 1), [[0, width // 3], [width // 2, width // 6],
                                        [width // 3, 0], [width // 6, width // 2]], 1)
    surf_torso = pygame.Surface((width, width))
    surf_torso.set_colorkey(BLACK)
    pygame.draw.circle(surf_torso, BLUE, (width*0.4, -width*0.45), width*0.6)
    pygame.draw.circle(surf_torso, (0, 0, 1), (width*0.4, -width*0.45), width*0.6, 1)
    surf_torso_up = pygame.transform.flip(surf_torso, 0, 1)
    torso = pygame.Surface((width, width))
    torso.blit(surf_torso, (0, width*0.3))
    torso.blit(surf_torso_up,(0, -width*0.7))
    torso.set_colorkey(BLACK)
    torso = pygame.transform.rotate(torso, -40)
    pygame.draw.polygon(torso, BLUE, [[width, width*0.7], [width*1.2,
                                            width*0.65], [width*1, width*0.9]])
    pygame.draw.polygon(torso, (0, 0, 1), [[width, width*0.7], [width*1.2,
                                            width*0.65], [width*1, width*0.9]], 1)

    surf_fish.blit(surf_fin,(width*0.4, width//3))
    surf_fish.blit(torso, (width*0, width*0.2))
    surf_fish.set_colorkey(BLACK)
    return surf_fish


def cat(width, coords):
    surf_cat = pygame.Surface((width, width/2))
    pygame.draw.ellipse(surf_cat, DARK_GREY, (width//8, width//4, width//2, width//10))
    nail = draw_ellipse(width*0.3, width*0.06, DARK_GREY)
    nail = pygame.transform.rotate(nail, 35)
    surf_cat.blit(nail, (width*0.57, width*0.11))
    leg = draw_ellipse(width*0.25, width*0.04, DARK_GREY)
    leg1 = pygame.transform.rotate(leg, -175)
    leg2 = pygame. transform.rotate(leg, -160)
    leg3 = pygame.transform.rotate(leg, -20)
    leg4 = pygame.transform.rotate(leg, -25)
    surf_cat.blit(leg1, (width*0, width*0.3))
    surf_cat.blit(leg2, (width*0.05, width*0.31))
    surf_cat.blit(leg3, (width*0.5, width*0.28))
    surf_cat.blit(leg4, (width*0.45, width*0.3))
    surf_fish = draw_fish(width//3)

    surf_head = pygame.Surface((width*0.3, width*0.3))
    surf_head.fill(RED)
    pygame.draw.ellipse(surf_head, DARK_GREY, (0, 0, width*0.16, width*0.12))
    pygame.draw.circle(surf_head, WHITE, (width*0.03, width*0.05), width*0.02)
    pygame.draw.circle(surf_head, (0, 0, 1), (width*0.04, width*0.05), width*0.01)
    pygame.draw.circle(surf_head, WHITE, (width*0.09, width*0.06), width*0.02)
    pygame.draw.circle(surf_head, (0, 0, 1), (width*0.10, width*0.06), width*0.01)
    surf_head.set_colorkey(RED)
    pygame.draw.polygon(surf_head, WHITE, [[width*0.035, width*0.11], [width*0.04, width*0.11],
                                              [width*0.0375, width*0.12]])
    pygame.draw.polygon(surf_head, WHITE, [[width * 0.07, width * 0.12], [width * 0.08, width * 0.12],
                                           [width * 0.075, width * 0.13]])
    pygame.draw.polygon(surf_head, (0, 0, 1), [[width * 0.04, width * 0.09], [width * 0.06, width * 0.09],
                                           [width * 0.05, width * 0.10]])

    surf_cat.blit(surf_fish, (-width*0.135, width*0.05))
    surf_cat.blit(surf_head, (width*0.1, width*0.15))
    surf_cat.set_colorkey(BLACK)
    pygame.draw.polygon(surf_cat, DARK_GREY, [[width * 0.15, width * 0.12], [width * 0.14, width * 0.18],
                                               [width * 0.22, width * 0.18]])
    pygame.draw.polygon(surf_cat, DARK_GREY, [[width * 0.22, width * 0.12], [width * 0.18, width * 0.18],
                                              [width * 0.25, width * 0.19]])
    screen.blit(surf_cat, coords)

    return screen


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    draw_background(screen, GREY, WHITE)
    igloo(400, 200, (50, 415), GREY)
    igloo(100, 50, (500, 100), GREY)
    igloo(200, 100, (250, 800), GREY)
    chukchi(400, (500, 550))
    chukchi(200, (100, 100))
    chukchi(100, (500, 100))
    cat(300, (100, 700))
    cat(200, (500, 850))
    pygame.display.update()

    clock.tick(FPS)