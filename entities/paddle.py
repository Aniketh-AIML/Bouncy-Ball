import pygame
from settings import *

class Paddle:

    def __init__(self):

        self.x = 340
        self.y = 550

        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT

        self.speed = PADDLE_SPEED

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if self.x < 0:
            self.x = 0

        if self.x + self.width > WIDTH:
            self.x = WIDTH - self.width

    def draw(self, surface):

        pygame.draw.rect(surface,(0, 0, 0),(self.x,self.y,self.width,self.height),border_radius=10)