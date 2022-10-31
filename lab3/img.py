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

car = pygame.image.load("imgs/car.png").convert() # создаем поверхность с изображением
car = pygame.transform.scale(car, (50, 50))
car_rect = car.get_rect(center=(WIDTH // 2, HEIGHT // 2))
car.set_colorkey((247, 247, 247)) # Делает белые пиксели прозрачными

car_right = car
car_down = pygame.transform.rotate(car, -90)
car_left = pygame.transform.flip(car, 1, 0)
car_up = pygame.transform.rotate(car, 90)

bg_surf = pygame.image.load("imgs/orange.jpg").convert() # рекомендуется делать .convert()
car = pygame.transform.scale(car, (50, 50)) # Масштабирует поверхность

car = car_right
speed = 5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    elif bt[pygame.K_RIGHT]:
        car = car_right
        car_rect.x += speed
        if car_rect.x > WIDTH - car_rect.height:
            car_rect.x = WIDTH - car_rect.height
    elif bt[pygame.K_UP]:
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif bt[pygame.K_DOWN]:
        car = car_down
        car_rect.y += speed
        if car_rect.y > HEIGHT - car_rect.height:
            car_rect.y = HEIGHT - car_rect.height

    screen.blit(bg_surf, (0, 0))
    screen.blit(car, car_rect)

    pygame.display.update()


    clock.tick(FPS)