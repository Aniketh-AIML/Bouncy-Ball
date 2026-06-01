import pygame
from settings import *

def load_background():

    background = pygame.image.load("resources/background_yellow.jpg")

    background = pygame.transform.scale(background,(WIDTH, HEIGHT))

    return background