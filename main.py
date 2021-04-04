import pygame
import sys
import math
import time as tm
import ui.classes as ui
import classes as pt

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
emmiter = pt.Emmiter((800, 450), pt.Particle((800, 450)))

#ARRAYS
ui_arr = [project_name_label, timer_label]
particle_array = []

#FUNCTIONS
def spawn_particles(amount, pos, radius):
    x,y = pos
    for i in range(amount):
        x1 = radius*math.sin(i * (2.0 * 3.14) / amount) + x
        y1 = radius*math.cos(i * (2.0 * 3.14) / amount) + y
        particle_array.append(pt.Particle((x1, y1)))

def force_pull(arr, pos):
    x,y = pos
    for particle in arr:
        try:
            mx = x-particle.position.x
            my = y-particle.position.y
            particle.force.x += mx
            particle.force.y += my
        except ZeroDivisionError:
            pass

# spawn_particles(50, (800, 450), 100)
# spawn_particles(50, (800, 450), 300)

#MAIN LOOP
while True:
    screen.fill(black)

    start = tm.time()

    emmiter.emit(particle_array)
    # force_pull(particle_array, (400, 300))
    # force_pull(particle_array, (1200, 600))


    for particle in particle_array:
        particle.update()
        # particle.draw_force(screen, green)
        particle.draw(screen, white)

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
