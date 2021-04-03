from math import cos, sin, sqrt
import pygame

g = 9.8

class Vector: #simple vector class, might update in future if needed

    x = int
    y = int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lenght(self):
        return math.sqrt(x**2 + y**2)

    def lenght2(self): #in some cases you don't need the square root
        return (x**2 + y**2)

    def tuple(self):
        return (self.x, self.y)

class Particle:

    position = Vector

    mass = 1.0

    force = Vector
    velocity = Vector
    acceleration = Vector

    lifetime = float

    #STATES
    sleeping = False
    colliding = False

    def __init__(self, pos):
        x,y = pos
        self.position = Vector(x, y)
        self.force = Vector(0,0)
        self.velocity = Vector(0,0)
        self.acceleration = Vector(0,0)
