import pygame
import sys
import Ghost
import Pacman
import Maze
import Grains
import car
import Score
import random

pygame.init()

black = (0, 0, 0)

size = width, height = 640, 800
screen = pygame.display.set_mode(size)
snow_list = []
for i in range(250):
    x = random.randrange(0, 640)
    y = random.randrange(-800, 0)
    snow_list.append([x, y])
clock = pygame.time.Clock()
def win():
    a = 1
    #тут победа, но её немаdef win():
def no_win():
    a = 1
    #тут поражение, но его тоже нема

def run_all(player_name):
    gameover = False
    time = 0
    tmp_time = time
    seeds = Grains.generateSeeds(Maze.walls)
    bigseeds = Grains.generateBigSeed()
    full = len(seeds) + len(bigseeds)
    # print(seeds)
    pacman = Pacman.Pacman()
    day = pygame.image.load("3.png").convert_alpha()
    flag_snow = False
    flag_hard = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Score.add_highscore(player_name, pacman.score)
                sys.exit()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('PACMAN')

        screen.fill(black)
        all_sprites_list = pygame.sprite.RenderPlain()
        ghost_factory = Ghost.create_ghosts()
        wall_list = Maze.setupRoomOne(all_sprites_list)
        gate = Maze.setupGate(all_sprites_list)
        # Логика

        # Убывание очков
        time += 1
        if time // 40 - tmp_time // 40 > 0 and pacman.score != 0:
            pacman.score -= 1
            tmp_time = time


        if not Ghost.Ghost.list[3].blue and full - (len(bigseeds) + len(seeds)) >= full / 3:
            Ghost.Ghost.list[3].activate()
        if not Ghost.Ghost.list[2].blue and full - (len(bigseeds) + len(seeds)) >= 30:
            Ghost.Ghost.list[2].activate()
        Ghost.move_all()
        Ghost.check_collide_all(pacman)
        if len(seeds) == 0:
            Score.add_highscore(player_name, pacman.score)
            gameover = True
        if pacman.lives == 0:
            Score.add_highscore(player_name, pacman.score)
            gameover = True
        pacman.update(Maze.walls, Maze.gate_list)
        Score.pacman_eats_grain(pacman, seeds)
        Score.pacman_eats_big_grain(pacman, bigseeds)
        # Отрисовка
        wall_list.draw(screen)
        pacman.draw(screen)
        gate.draw(screen)
        Score.text_on_screen(screen, f"Top Personal Score", 180, 0)
        Score.text_on_screen(screen, str(Score.get_top_score(player_name)), 270, 35)
        Score.text_on_screen(screen, f"Score: {pacman.score}", 10, 30)
        Score.show_pacman_lives(screen, pacman.lives)
        Ghost.Ghost.list[0].draw(screen)
        Ghost.Ghost.list[1].draw(screen)
        Ghost.Ghost.list[2].draw(screen)
        Ghost.Ghost.list[3].draw(screen)

        block_list = pygame.sprite.RenderPlain()
        monsta_list = pygame.sprite.RenderPlain()
        pacman_collide = pygame.sprite.RenderPlain()
        gate = Maze.setupGate(all_sprites_list)
        for seed in seeds:
            seed.draw(screen)
        for seed in bigseeds:
            seed.draw(screen)
        # обработка каждой снежинки
        if flag_snow == True:
            for i in range(len(snow_list)):

                # нарисовать снежинку
                pygame.draw.circle(screen, (255,255,255), snow_list[i], 2)

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
        if pygame.key.get_pressed()[pygame.K_n]:
            flag_hard = True
        if pygame.key.get_pressed()[pygame.K_m]:
            flag_hard = False

        if flag_hard == True:
            screen.blit(day, (-1885 + pacman.rect.x, -1590 + pacman.rect.y))
        #-
        # print(Ghost.Ghost.list[0].type, Ghost.Ghost.list[1].type)
        # print(Ghost.Ghost.list[2].type, Ghost.Ghost.list[3].type)
        # print(pacman.rect.x, pacman.rect.y)

        clock.tick(40)
        pygame.display.flip()
        pygame.time.wait(10)


def main():
    run_all()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
