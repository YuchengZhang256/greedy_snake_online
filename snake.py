import pygame
from settings import Settings

class Snake:
    def __init__(self, sequence_number,ai_game):
        """the sequence number determines which player to manipulate this snake, for now this number is 0 or 1"""
        self.screen = ai_game.screen
        self.snake_speed = 5
        self.block = 10
        self.length = 1
        self.list = []
        self.settings = Settings()
        self.x = self.settings.screen_length * sequence_number
        self.y = self.settings.screen_height * sequence_number
        
        
    def draw_snake(self):
        for x in self.list:
            pygame.draw.rect(self.screen, self.settings.snake_color, [x[0], x[1], self.block, self.block])
        