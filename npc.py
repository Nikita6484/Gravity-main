import pygame
import math

# Установка красного цвета для шарика
RED = (255, 8, 8)

# Инициализация Pygame
pygame.init()

# Ввод пользовательских данных
user_input_height = float(input("Введите высоту, с которой шарик начинает движение вниз >>> "))
user_input_radius = float(input("Введите радиус шара >>> "))
user_input_mass = float(input("Введите массу шара >>> "))

# Настройки экрана
display_width = 400
display_height = 400

# Начальное положение шарика
x_position = display_width // 2 - 15
y_position = user_input_height

# Создание экрана
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ball")
clock = pygame.time.Clock()


# Функция вычисления гравитационного ускорения для шарика с учетом его массы
def gravity(height, mass):
    g = 9.81
    acceleration = g * mass
    time = math.sqrt(2 * height / acceleration)
    speed = acceleration * time
    return time, speed


# Функция обработки падения шарика
def fall():
    global y_position, speed
    time, new_speed = gravity(display_height - user_input_radius - y_position, user_input_mass)
    y_position += new_speed
    speed = new_speed
    if y_position + user_input_radius >= display_height and speed > 0:
        y_position = display_height - user_input_radius
        speed = 0
        kinetic_energy = 0.5 * user_input_mass * speed ** 2
        print(
            f"Шарик коснулся нижней поверхности за {time:.2f} секунд. Кинетическая энергия в этот момент: {kinetic_energy:.2f} Дж"
            )


# Главный игровой цикл
running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    fall()

    # Отрисовка шарика на экране
    pygame.draw.circle(screen, RED, (x_position, int(y_position)), user_input_radius)

    pygame.display.update()