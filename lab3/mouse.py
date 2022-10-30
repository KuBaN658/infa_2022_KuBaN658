import pygame

pygame.init()

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("События от мыши")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
pygame.mouse.set_visible(False) # скрывает указатель мыши
FPS = 60
clock = pygame.time.Clock()
start_paint = None # координаты левого верхнего угла прямоугольника
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(WHITE)

    pos = pygame.mouse.get_pos() # кортеж координат указателя мыши
    if pygame.mouse.get_focused(): # если указатель мыши находится в окне
        pygame.draw.circle(screen, RED, pos, 5) # красный круг на месте указателя
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("Нажата кнопка: ", event.button) # выводит номер нажатой кнопки
    elif event.type == pygame.MOUSEMOTION:
        print("Позиция мыши: ", event.pos)   # pos(абсолютные) | rel(относительные координаты)
    pressed = pygame.mouse.get_pressed() # кортеж показывающий нажатую кнопку
    if pressed[0]:  # под индексом 0 левая кнопка мыши

        if start_paint is None: # при нажатии кнопки присваиваем координаты
            start_paint = pos

        width = pos[0] - start_paint[0]
        height = pos[1] - start_paint[1]

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (start_paint[0], start_paint[1], width, height))

    else:
        start_paint = None
    pygame.display.update()
    clock.tick(FPS)