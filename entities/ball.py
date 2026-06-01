import pygame
from settings import *

class Ball:

    def __init__(self):

        self.radius = BALL_RADIUS

        self.reset()

    def reset(self):

        self.x = 10
        self.y = 100

        self.vx = BALL_SPEED_X
        self.vy = BALL_SPEED_Y

    def update(self):

        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < 0:
            self.vx = -self.vx

        if self.x + self.radius > WIDTH:
            self.vx = -self.vx

        if self.y - self.radius < 0:
            self.vy = -self.vy

    def draw(self, surface):

        pygame.draw.circle(surface,(150, 75, 0),(int(self.x),int(self.y)),self.radius)