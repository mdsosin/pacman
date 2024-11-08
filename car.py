import pygame
import math
import time

def timer(img, rec, fin, scr):
    start_ticks = pygame.time.get_ticks() #starter tick
    size = width, height = 640, 800
    screen = pygame.display.set_mode(size)
    while True: # mainloop
        seconds = (pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        if seconds >= 10: # if more than 10 seconds close the game
            break
        #-----------------------------
        #добавить сюда открисовку скрина
        screen.blit(scr, (0, 0))
        #-----------------------------
        f2 = pygame.font.SysFont('serif', 148)
        text2 = f2.render(str(int(10 - seconds)), True, (0, 180, 0))
        #screen.fill((255,255,255))
        screen.blit(text2, (270,150))
        screen.blit(img, rec)
        screen.blit(fin, (310,510))
        pygame.display.flip()

def rotate(img, pos, angle):
    w, h = img.get_size()
    img2 = pygame.Surface((w*2, h*2), pygame.SRCALPHA)
    img2.blit(img, (w-pos[0], h-pos[1]))
    return pygame.transform.rotate(img2, angle)

def main_p():
    size = width, height = 640, 800
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    game_over = False
    pygame.display.set_caption('GG')
    imagec = pygame.image.load("img.png").convert_alpha()
    finish = pygame.image.load("finish.png").convert_alpha()
    sren = pygame.image.load("screenshot.jpg").convert_alpha()
    pivod = (300, 200) # положение центра вращения на экране
    x, y = 300, 200
    angle = 0
    center_image = (100,130) # положение центра вращения на изображении
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        if pygame.key.get_pressed()[pygame.K_s]:
            x -=  3*math.cos(math.radians(270-angle))
            y -=  3*math.sin(math.radians(270-angle))
        if pygame.key.get_pressed()[pygame.K_w]:
            x += 3*math.cos(math.radians(270-angle))
            y += 3*math.sin(math.radians(270-angle))
        if pygame.key.get_pressed()[pygame.K_d]:
            angle -= 1 % 360
        if pygame.key.get_pressed()[pygame.K_a]:
            angle += 1 % 360
        #screen.fill(white)
        screen.blit(sren, (0, 0))
        #------------------------
        pivod = (x,y)
        image = rotate(imagec, center_image , angle)
        rect = image.get_rect()
        rect.center = pivod
        screen.blit(image, rect)
        screen.blit(finish, (310,510))
        #------------------------
        #pygame.draw.rect(screen, (0,0,0), rec)
        pygame.display.flip()
        if(y>=800 and x>=400 and x<=640):
            timer(image, rect,finish, sren)
            game_over = True
        if(y>=820 or y<=-20 or x<=-20 or x>=660):
            x,y= 300, 250
        pygame.display.flip()
    #pygame.quit()

 
if __name__ == '__main__':
    main_p()