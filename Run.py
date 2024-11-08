import pygame, car
import sys, random
import webbrowser
from pacman_scenes import MainScene, MenuScene, TableScene, ReplayScene, PauseScene, InputBox, SkinChangeScene, ImageBox
from pacman_scenes.constants_pacman import *
from pathlib import Path

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# пустой список5
snow_list = []

# Пройдемся 50 раз циклом и добавьм снежинки в рандомную позицию x,y
for i in range(250):
    x = random.randrange(0, 640)
    y = random.randrange(-800, 0)
    snow_list.append([x, y])

clock = pygame.time.Clock()
# этот файл создан исключительно для того, чтобы продемонстрировать работу "сцен"
# потом скорее всего придется его удалить

def donate(current_scene):
    if current_scene == MENU_SCENE_INDEX:
        buttons = pygame.key.get_pressed()
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
        if buttons[pygame.K_LCTRL]:
            if buttons[pygame.K_q]:
                webbrowser.open_new_tab('https://qiwi.com/p/79854723577')

def run_scenes():
    pygame.init()
    pygame.font.init()

    if not Path("high_scores.txt").is_file():
        with open('high_scores.txt', 'w') as hsf:
            hsf.write("NAME SCORE\n")

    screen = pygame.display.set_mode(SIZE)

    MENU_SCENE = MenuScene(screen)
    TABLE_SCENE = TableScene(screen)
    MAIN_SCENE = MainScene(screen)
    REPLAY_SCENE = ReplayScene(screen)
    PAUSE_SCENE = PauseScene(screen)
    SKIN_SCENE = SkinChangeScene(screen)

    scene = [MENU_SCENE, TABLE_SCENE, MAIN_SCENE, REPLAY_SCENE, PAUSE_SCENE, SKIN_SCENE]
    current_scene = MENU_SCENE_INDEX
    game_over = False
    flag_snow = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # events - функция - обработка события для каждого объекта функции
            for obj in scene[current_scene].objects:
                obj.events(event)

        # функции каждой "сцены", помогает с кнопочками
        for f in scene[current_scene].logic_functions:
            f()

        screen.fill(background_color)
        # отрисовка каждого объекта текущей "сцены"
        for obj in scene[current_scene].objects:
            obj.draw()
            # Подтверждение отрисовки и ожидание
        # обработка каждой снежинки
        if flag_snow == True:
            for i in range(len(snow_list)):

                # нарисовать снежинку
                pygame.draw.circle(screen, WHITE, snow_list[i], 2)

                # снежинка вниз на 1
                snow_list[i][1] += 1

                if snow_list[i][1] > 800:
                    y = random.randrange(-50, 0)
                    snow_list[i][1] = y
                    x = random.randrange(0, 640)
                    snow_list[i][0] = x
        #Конец снежинок
        #- Неважно
        rect = pygame.Rect(0, 0, 800, 600)
        sub = pygame.Surface((640, 800))
        sub.blit(screen, rect)
        pygame.image.save(sub, "screenshot.jpg")
        if pygame.key.get_pressed()[pygame.K_c]:
            car.main_p()
        if pygame.key.get_pressed()[pygame.K_p]:
            car.win()
        if pygame.key.get_pressed()[pygame.K_o]:
            car.no_win()
        if pygame.key.get_pressed()[pygame.K_l]:
            flag_snow = True
        if pygame.key.get_pressed()[pygame.K_k]:
            flag_snow = False
        #-
        donate(current_scene)

        clock.tick(40)
        pygame.display.flip()
        pygame.time.wait(10)

        # обновление "сцены"
        current_scene = scene[current_scene].update()

        # здесь потом нужно будет написать обработку конца main и вызвать функцию end_of_main
    sys.exit()


if __name__ == '__main__':
    run_scenes()
