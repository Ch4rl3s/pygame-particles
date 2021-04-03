import pygame
import sys
import math
import time as tm
import ui.classes as ui
import classes as rc

mainClock = pygame.time.Clock()

screen_size = [1600,900]

black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)
green = (0, 255 , 0)
red = (255 , 0, 0)
grey = (10,10,10,255)

pygame.init()

myfont = pygame.font.SysFont('timesnewroman',  12)

pygame.display.set_caption('pygame particle library')
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
screen.fill(white)

#STATES
mouse_down = False

#OBJECTS
project_name_label = ui.Label(10, 10, "particles")
timer_label = ui.Label(10, 25, "timer label")

#ARRAYS
ui_arr = [project_name_label, timer_label]

while True:
    screen.fill(black)

    start = tm.time()

    end = tm.time()
    timer_label.text = f"{round((end - start), 5)}"

    for element in ui_arr:
        element.render(screen, white, myfont)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for element in ui_arr:
            element.check_input(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()


        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

    pygame.display.update()
    mainClock.tick(360)
