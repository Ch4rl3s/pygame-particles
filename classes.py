from math import cos, sin, sqrt
import pygame
from random import randint, uniform

g = 9.8
dt = 0.001

screenx, screeny = 1600,900

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

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y

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

    def new(self):
        particle = Particle(self.position.tuple())
        particle.velocity = self.velocity
        particle.force = self.force
        return particle

    def __init__(self, pos):
        x,y = pos
        self.position = Vector(x, y)
        self.force = Vector(0,0)
        self.velocity = Vector(0,0)
        self.acceleration = Vector(0,0)

    def draw_force(self, screen, colour):
        mx = self.position.x + self.velocity.x
        my = self.position.y + self.velocity.y
        pygame.draw.aaline(screen, colour, self.position.tuple(), (mx, my))

    def draw(self, screen, colour):
        pygame.draw.circle(screen, colour, self.position.tuple(), 1)

    def update(self):
        self.IntegrateEuler()
        pass

    def IntegrateEuler(self):
#x
        self.velocity.x += self.force.x/self.mass*dt
        self.position.x +=  self.velocity.x*dt
        if self.position.x > screenx:
            self.position.x = screenx
            self.velocity.x = -self.velocity.x
        elif self.position.x < 0:
            self.position.x=0
            self.velocity.x = -self.velocity.x
        mx = 800 - self.position.x
        my = 450 - self.position.y
        m =sqrt(mx**2 + my**2)
        if m>400:
            # self.position.x -=  self.velocity.x*dt
            self.velocity.x = -self.velocity.x
            # self.position.y -=  self.velocity.y*dt
            self.velocity.y = -self.velocity.y

#y
        self.velocity.y += self.force.y/self.mass*dt
        self.position.y +=  self.velocity.y*dt
        if self.position.y > screeny:
            self.position.y = screeny
            self.velocity.y = -self.velocity.y
        elif self.position.y < 0:
            self.position.y=0
            self.velocity.y = -self.velocity.y

class Emmiter:

    position = Vector

    particle = Particle

    initial_velocity = Vector
    time_interval = float

    def __init__(self, pos, particle):
        x,y = pos
        self.position = Vector(x, y)
        self.particle = particle.new()

    def emit(self, arr):
        particle = Particle(self.particle.position.tuple())
        x = uniform(-50.0, 50.0)
        y = uniform(-50.0, 50.0)
        particle.force.x += x
        particle.force.y += y
        arr.append(particle)
