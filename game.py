import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))

# Название окна
pygame.display.set_caption("Моя игра")

# Цвет фона
bg_color = (255, 255, 255)

# Определение класса для игровых объектов
class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    # Функция для проверки столкновений с другими объектами
    def collides_with(self, other_object):
        return self.rect.colliderect(other_object.rect)

# Создание игровых объектов
player = GameObject(100, 100, 50, 50)
enemy = GameObject(200, 200, 50, 50)

# Обновление экрана
def redraw_game_window():
    win.fill(bg_color)
    # Отрисовка игровых объектов
    pygame.draw.rect(win, (255, 0, 0), player.rect)
    pygame.draw.rect(win, (0, 255, 0), enemy.rect)
    pygame.display.update()

# Основной цикл программы
run = True
while run:
    # Получение событий из очереди
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Обработка пользовательского ввода
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    
    # Проверка столкновений игровых объектов
    if player.collides_with(enemy):
        print("Столкновение!")
    
    # Обновление координат игровых объектов
    player.rect.x = player.x
    player.rect.y = player.y
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.y
    
    # Отрисовка игровых объектов
    redraw_game_window()

# Закрытие окна Pygame
pygame.quit()
