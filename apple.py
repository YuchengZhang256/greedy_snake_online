import pygame
import random
from pygame.sprite import Sprite


class Apple(Sprite):
    
    def __init__(self,ai_game):
        """initialize an apple"""
        super().__init__()
        self.settings = ai_game.settings 
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.apple_color
        self.apple_x = round(random.randrange(0, 1800 - 10) / 10.0) * 10.0
        self.apple_y = round(random.randrange(0, 1200 - 10) / 10.0) * 10.0
        

    def draw_apple(self):
        """draw the apple on the screen"""
        pygame.draw.rect(self.screen, self.color, [self.apple_x, self.apple_y, 10, 10])
        

        