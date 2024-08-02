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
        self.length = self.settings.apple_length
        self.height = self.settings.apple_height
        self.color = self.settings.apple_color
        
        """generate the position of the apple randomly, on both x-axis and  y-axis"""
        rand_position_x = random.randint(200,1600)
        rand_position_y = random.randint(100,1000)
        self.rect = pygame.Rect(rand_position_x, rand_position_y, self.length, self.height)
        
        
    def draw_apple(self):
        """draw the apple on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        

        