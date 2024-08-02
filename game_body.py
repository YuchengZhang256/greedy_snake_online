import sys
import pygame
from settings import Settings
from apple import Apple


class Greedy_Snakes:
    """initialize the game"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_length, self.settings.screen_height))
        pygame.display.set_caption("Greedy Snakes")
        
        
        