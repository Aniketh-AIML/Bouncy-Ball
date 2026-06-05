import pygame
from settings import *

class Ball:

    def __init__(self):

        self.radius = BALL_RADIUS

        self.reset()

        # Remember original speed
        self.base_vx = BALL_SPEED_X
        self.base_vy = BALL_SPEED_Y

    def reset(self):

        self.x = WIDTH // 2
        self.y = 100

        self.vx = BALL_SPEED_X
        self.vy = BALL_SPEED_Y

    def increase_speed(self):

        # Current maximum allowed speeds
        max_vx = self.base_vx * BALL_MAX_SPEED_MULTIPLIER
        max_vy = self.base_vy * BALL_MAX_SPEED_MULTIPLIER

        # Increase speed by 5%
        self.vx *= BALL_SPEED_MULTIPLIER
        self.vy *= BALL_SPEED_MULTIPLIER

        # Cap the speed
        if abs(self.vx) > max_vx:
            self.vx = max_vx if self.vx > 0 else -max_vx

        if abs(self.vy) > max_vy:
            self.vy = max_vy if self.vy > 0 else -max_vy

    def update(self):

        wall_hit = False

        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < 0:
            self.vx = -self.vx
            wall_hit = True

        if self.x + self.radius > WIDTH:
            self.vx = -self.vx
            wall_hit = True

        if self.y - self.radius < 0:
            self.vy = -self.vy
            wall_hit = True

        return wall_hit

    def draw(self, surface):

        pygame.draw.circle(surface,(150, 75, 0),(int(self.x),int(self.y)),self.radius)