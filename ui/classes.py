import pygame
import math

class Label:
    x = int
    y = int
    # width = int
    # height = int
    draw_tr = False

    text = ''

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        # self.height = height
        # self.width = width
        self.text = text

    def render(self, screen, colour, font):
        text = font.render(self.text, False, colour)
        screen.blit(text, (self.x, self.y))

    def check_input(self, event):
        pass

class Button:

    x = int
    y = int
    height = int
    width = int

    #TEXT PROPERTIES
    text = ''
    font_size = 12

    #STATES
    pressed = False

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, screen, colour, font):
        if self.text!='':
            self.width=len(self.text*self.font_size)/2
        if self.pressed==False:
            pygame.draw.rect(screen, colour, (self.x, self.y, self.width, self.height), width=1)
        elif self.pressed:
            pygame.draw.rect(screen, colour, (self.x, self.y, self.width, self.height), width=4)
        text = font.render(self.text, False, colour)
        screen.blit(text, (self.x+self.font_size/2, self.y))

    def coords_in(self,coords):
        x, y = coords
        if (self.x < x < self.x+self.width) and (self.y < y < self.y+self.height):
            return True
        else:
            return False

    def check_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.coords_in(pygame.mouse.get_pos()):
                self.pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
        if self.coords_in(pygame.mouse.get_pos())==False:
            self.pressed = False
