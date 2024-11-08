import pygame
import Ghost

# Соритровка листа по очкам
def sort_list_by_second_elem(sub_li):
    return (sorted(sub_li, reverse = True, key=lambda x: x[1]))

# Функции передаётся класс пакмана и лист зёрен. Зерно удаляется, очки увеличиваются.
def pacman_eats_grain(pacman, grains_list):
    for item in grains_list:
        if pacman.rect.colliderect(item.rect):
            grains_list.remove(item)
            pacman.score += 10


def pacman_eats_big_grain(pacman, grains_list):
    for item in grains_list:
        if pacman.rect.colliderect(item.rect):
            grains_list.remove(item)
            Ghost.blue_mode()

# Выводит текст text на экран по координатам x и y. x и y указывают левый верхний угол прямоугольника с текстом.
def text_on_screen(screen, text, x, y):
    pygame.font.init()
    text_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = text_font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))


# Добавить новый результат по очкам.
def add_highscore(player_name, score):
    with open('high_scores.txt', 'r') as highscore_file:
        lines = [line.strip().split(' ') for line in highscore_file.readlines()]
    if len(lines) == 1:
        with open('high_scores.txt', 'a') as hsf:
            hsf.write(f"{player_name} {score}\n")
    if len(lines) > 1:
        lines.append([player_name, score])

        lines = lines[1:]

        for line in lines:
            line[1] = int(line[1])

        lines = sort_list_by_second_elem(lines)
        lines.insert(0, ["NAME", "SCORE"])

        with open('high_scores.txt', 'w') as hsf:
            for line in lines:
                hsf.write(f"{line[0]} {line[1]}\n")


# Возвращает top score из файла с highscore'ми
def get_top_score(player_name):
    with open('high_scores.txt', 'r') as highscore_file:
        lines = [line.strip().split(' ') for line in highscore_file.readlines()]
        if len(lines) == 1: return 0
        if len(lines) > 1:
            for line in lines:
                if line[0] == player_name:
                    return line[1]
            return 0


def render_life(screen, x, y):
    life_image = pygame.image.load('img/Pacman/pacman_40x40.png')
    life_rect = life_image.get_rect()
    life_rect.x = x
    life_rect.y = y
    screen.blit(life_image, life_rect)


def show_pacman_lives(screen, pacman_lives):
    if pacman_lives < 1:
        return 0

    else:
        x = 10
        for i in range(pacman_lives - 1):
            render_life(screen, x, 755)
            x += 50
