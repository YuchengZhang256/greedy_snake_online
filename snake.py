import pygame
from settings import Settings

class Snake:
    def __init__(self, sequence_number,ai_game):
        """the sequence number determines which player to manipulate this snake, for now this number is 0 or 1"""
        self.screen = ai_game.screen
        self.block = 40
        self.length = 1
        self.list = []
        self.settings = Settings()
        
        """initialize the position of this snake due to its sequence number is 0 or 1"""
        self.x = self.settings.screen_length * sequence_number/2
        self.y = self.settings.screen_height * sequence_number/2
        
        """the initial state of this snake is still, you should use the keyboard to make it move"""
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        self.moving_right =False
        
        
    def draw_snake(self):
        for x in self.list:
            pygame.draw.rect(self.screen, self.settings.snake_color, [x[0], x[1], self.block, self.block])
        