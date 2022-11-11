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
HEAD_COLOR = (172, 157, 147)
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
    draw_snow_brick(surf_jurt, width, height, width//9, width//6)

    screen.blit(surf_jurt, coords)


def draw_contour(width, height, color):
    """
    рисует очертание иглу
    :param width: ширина иглу
    :param height: высота иглу
    :param color: цвет иглу
    :return: возвращает поверхность с нарисованным очертанием иглу
    """
    surf_jurt = pygame.Surface((width, height))
    surf_jurt.fill(TEMP_COLOR)
    pygame.draw.circle(surf_jurt, color, (height, height), height)
    pygame.draw.circle(surf_jurt, BLACK, (height, height), height, 2)
    surf_jurt.set_colorkey(TEMP_COLOR)
    return surf_jurt


def draw_snow_brick(surf_jurt, width, height, height_brick, weight_brick):
    """
    Рисует кирпичики на поверхности иглу
    :param surf_jurt: поверхность с нарисованным очертанием
    :param width: ширина иглу
    :param height: высота иглу
    :param height_brick: высота кирпичиков
    :param weight_brick: ширина кирпичиков
    :return: None
    """
    x = 0
    y = width // 2 - 1
    h = 0 # расстояние от основания иглы до рисуемой горизонтали
    pygame.draw.line(surf_jurt, BLACK, (x, y), (width - x, y)) #рисуем горизонталь
    for i in range(height//height_brick):
        y = y - height_brick
        h += height_brick
        x = height - (height ** 2 - h ** 2) ** 0.5 + 1
        pygame.draw.line(surf_jurt, BLACK, (x, y), (width - x, y))
        x1 = x + weight_brick // 2
        y1 = y
        x2 = x + weight_brick // 2
        y2 = y + height_brick
        while x1 < width - x:
            pygame.draw.line(surf_jurt, BLACK, (x1, y1), (x2, y2))
            x1 += weight_brick
            x2 += weight_brick
    pygame.draw.line(surf_jurt, BLACK, (height, y), (height, 0))


def draw_ellipse(width, height, color):
    """
    Рисует овал
    :param width: ширина овала
    :param height: высота овала
    :param color: цвет овала
    :return: возвращает поверхность с нарисованным овалом
    """
    surf_ellipse = pygame.Surface((width, height))
    pygame.draw.ellipse(surf_ellipse, color, (0, 0, width, height))
    surf_ellipse.set_colorkey(BLACK)
    return surf_ellipse


def chukchi(width, height, coords):
    """
    Рисует чукчу
    :param height: высота чукчи
    :param width: ширина чукчи
    :param coords: координаты левого верхнего угла поверхности чукчи
    :return: None
    """
    surf_chukchi = pygame.Surface((width, height))
    surf_chukchi.fill(TEMP_COLOR)
    pygame.draw.ellipse(surf_chukchi, BEIGE, (width*0.215, 0, width*0.5, height*0.3)) #задний фон головы
    draw_legs(surf_chukchi, width, height)
    draw_hands(surf_chukchi, width, height)
    draw_torso(surf_chukchi, width, height)
    draw_head(surf_chukchi, width, height)
    pygame.draw.line(surf_chukchi, BLACK, (width*0.03, 0), (width*0.08, height)) #Рисуем посох

    surf_chukchi.set_colorkey(TEMP_COLOR)
    screen.blit(surf_chukchi, coords)


def draw_torso(surface, width, height):
    """
    рисует туловище чукчи
    :param surface: поверхность для рисования
    :param width: ширина чукчи
    :param height: высота чукчи
    :return: None
    """
    torso = pygame.Surface((width // 1.3, height*0.7))
    pygame.draw.ellipse(torso, BROWN, (0, 0, width // 1.3, height * 1.4))
    pygame.draw.rect(torso, DARK_BROWN, (0, height * 0.65, width * 0.8, height * 0.05))
    pygame.draw.rect(torso, DARK_BROWN, (width * 0.28, height * 0.1, width * 0.2, height * 0.7))
    torso.set_colorkey(BLACK)
    surface.blit(torso, (width * 0.095, width * 0.18))


def draw_legs(surface, width, height):
    """
    рисует ноги чукчи
    :param surface: поверхность для рисования
    :param width: ширина чукчи
    :param height: высота чукчи
    :return: None
    """
    leg = draw_ellipse(width // 6, height // 3.5, BROWN)
    surface.blit(leg, (width // 4, height * 0.65))
    surface.blit(leg, (width // 1.8, height * 0.65))
    foot = draw_ellipse(width // 4, height // 14, BROWN)
    surface.blit(foot, (width // 6, height * 0.9))
    surface.blit(foot, (width // 1.8, height * 0.9))


def draw_head(surface, width, height):
    """
    Рисует голову чукчи
    :param surface: поверхность для рисования
    :param width: ширина чукчи
    :param height: высота чукчи
    :return: None
    """
    pygame.draw.ellipse(surface, HEAD_COLOR,
                        (width * 0.27, height * 0.04, width * 0.4, height * 0.25))
    pygame.draw.ellipse(surface, BEIGE,
                        (width * 0.32, height * 0.07, width * 0.3, height * 0.19))
    pygame.draw.line(surface, BLACK, (width * 0.37, height * 0.11), (width * 0.43, height * 0.13))
    pygame.draw.line(surface, BLACK, (width * 0.5, height * 0.13), (width * 0.56, height * 0.11))
    pi = 3.14
    pygame.draw.arc(surface, BLACK, (width * 0.42, height * 0.18, width * 0.1, height * 0.05), 0, pi)


def draw_hands(surface, width, height):
    """
    Рисует руки чукчи
    :param surface: поверхность для рисования
    :param width: ширина чукчи
    :param height: высота чукчи
    :return: None
    """
    hand = draw_ellipse(width // 2.5, height // 12, BROWN)
    surface.blit(hand, (0, height // 4))
    hand_left = pygame.transform.rotate(hand, 150)
    surface.blit(hand_left, (width // 1.8, height // 4.5))





def cat(width, coords):
    """
    рисует бегущего кота с рыбой
    :param width: ширина кота
    :param coords: координаты левого верхнего угла на главной поверхности
    :return: None
    """
    height = width/2
    surf_cat = pygame.Surface((width, height))
    surf_cat.fill(TEMP_COLOR)
    draw_torso_nail_leg_of_cat(surf_cat, width, height)
    draw_fish(surf_cat, width//3, height//3)
    draw_cat_head(surf_cat, width, height)
    surf_cat.set_colorkey(TEMP_COLOR)
    screen.blit(surf_cat, coords)


def draw_torso_nail_leg_of_cat(surface, width, height):
    """
    Рисует туловище кота c лапами и хвостом
    :param surface: поверхность для рисования
    :param width: ширина кота
    :param height: высота кота
    :return: None
    """
    torso = draw_ellipse(width*0.6, height*0.25, DARK_GREY)
    surface.blit(torso, (width*0.2, height*0.5))
    nail = draw_ellipse(width*0.3, height*0.1, DARK_GREY)
    nail = pygame.transform.rotate(nail, 40)
    surface.blit(nail, (width*0.73, height*0.25))
    leg = draw_ellipse(width*0.3, height*0.06, DARK_GREY)
    leg1 = pygame.transform.rotate(leg, -175)
    leg2 = pygame. transform.rotate(leg, -160)
    leg3 = pygame.transform.rotate(leg, -20)
    leg4 = pygame.transform.rotate(leg, -25)
    surface.blit(leg1, (width*0, height*0.6))
    surface.blit(leg2, (width*0.05, height*0.62))
    surface.blit(leg3, (width*0.7, height*0.58))
    surface.blit(leg4, (width*0.65, height*0.6))


def draw_fish(surface, width, height):
    """
    Рисует рыбу
    :param surface: поверхность для рисования
    :param width: ширина кота
    :param height: высота кота
    :return: None
    """
    surf_fish = pygame.Surface((width*1.5, height*3))
    surf_fish.fill(TEMP_COLOR)
    draw_fin(surf_fish, width, height)
    draw_torso_fish(surf_fish, width, height)
    surf_fish.set_colorkey(TEMP_COLOR)
    surface.blit(surf_fish, (width*0, height*0.9))


def draw_fin(surface, width, height):
    """
    Рисует плавник рыбы
    :param surface: поверхность для ривования
    :param width: ширина кота
    :param height: высота кота
    :return: None
    """
    surf_fin = pygame.Surface((width // 2, width // 2))
    surf_fin.fill(TEMP_COLOR)
    pygame.draw.polygon(surf_fin, RED, [[0, height*0.5], [width // 2, height // 6],
                                        [width*0.3, 0], [width*0.2, height]])
    pygame.draw.polygon(surf_fin, BLACK, [[0, height*0.5], [width // 2, height // 6],
                                              [width*0.3, 0], [width*0.2, height]], 1)
    surf_fin.set_colorkey(TEMP_COLOR)
    surface.blit(surf_fin, (width * 0.3, height // 2))


def draw_torso_fish(surface, width, height):
    """
    Рисует тело рыбы
    :param surface: поверхность для рисования
    :param width: ширина кота
    :param height: высота кота
    :return: None
    """
    surf_torso = pygame.Surface((width, width))
    surf_torso.fill(TEMP_COLOR)
    pygame.draw.circle(surf_torso, BLUE, (width * 0.4, -width * 0.45), width * 0.6)
    pygame.draw.circle(surf_torso, BLACK, (width * 0.4, -width * 0.45), width * 0.6, 1)
    surf_torso_up = pygame.transform.flip(surf_torso, False, True)
    torso = pygame.Surface((width, width))
    torso.fill(TEMP_COLOR)
    torso.blit(surf_torso, (0, width * 0.3))
    torso.blit(surf_torso_up, (0, -width * 0.7))
    torso = pygame.transform.rotate(torso, -40)
    pygame.draw.polygon(torso, BLUE, [[width, width * 0.7], [width * 1.2,
                                                             width * 0.65], [width * 1, width * 0.9]])
    pygame.draw.polygon(torso, BLACK, [[width, width * 0.7], [width * 1.2,
                                                                  width * 0.65], [width * 1, width * 0.9]], 1)
    torso.set_colorkey(TEMP_COLOR)

    surface.blit(torso, (-width * 0.12, height * 0.04))


def draw_cat_head(surface, width, height):
    """
    Рисует голову кота
    :param surface: поверхность для рисования
    :param width: ширина кота
    :param height: высота кота
    :return: None
    """
    surf_head = pygame.Surface((width * 0.3, width * 0.3))
    surf_head.fill(TEMP_COLOR)
    pygame.draw.ellipse(surf_head, DARK_GREY, (0, 5, width * 0.16, width * 0.12))
    pygame.draw.circle(surf_head, WHITE, (width * 0.04, width * 0.05), width * 0.02)
    pygame.draw.circle(surf_head, BLACK, (width * 0.04, width * 0.05), width * 0.01)
    pygame.draw.circle(surf_head, WHITE, (width * 0.09, width * 0.06), width * 0.02)
    pygame.draw.circle(surf_head, BLACK, (width * 0.10, width * 0.06), width * 0.01)
    surf_head.set_colorkey(TEMP_COLOR)
    pygame.draw.polygon(surf_head, WHITE, [[width * 0.035, width * 0.11], [width * 0.04, width * 0.11],
                                           [width * 0.0375, width * 0.12]])
    pygame.draw.polygon(surf_head, WHITE, [[width * 0.07, width * 0.12], [width * 0.08, width * 0.12],
                                           [width * 0.075, width * 0.13]])
    pygame.draw.polygon(surf_head, BLACK, [[width * 0.04, width * 0.09], [width * 0.06, width * 0.09],
                                               [width * 0.05, width * 0.10]])
    pygame.draw.polygon(surf_head, DARK_GREY, [[width * 0.09, width * 0], [width * 0.12, width * 0.02],
                                             [width * 0.08, width * 0.02]])
    pygame.draw.polygon(surf_head, DARK_GREY, [[width * 0.02, width * 0], [width * 0.06, width * 0.02],
                                             [width * 0.03, width * 0.03]])
    surf_head = pygame.transform.rotate(surf_head, -20)
    surface.blit(surf_head, (width * 0.13, height * 0.3))


def main():
    draw_background(screen, GREY, WHITE)
    igloo(400, 200, (50, 415), GREY)
    chukchi(200, 300, (500, 500))
    cat(300, (100, 700))



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    main()
    pygame.display.update()

    clock.tick(FPS)