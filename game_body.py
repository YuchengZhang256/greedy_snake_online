import sys
import pygame

from settings import Settings
from apple import Apple
from snake import Snake


class GreedySnakes:
    """initialize the game"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_length, self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Greedy Snakes")
        self.snake_0 = Snake(0,self)
        self.snake_1 = Snake(1,self)
        self.apples = pygame.sprite.Group()
        self.creat_apples()
        self.apples_amount = self.settings.init_apples_amount
        self.game_active = True
        self.winner = ""
    
    
    def creat_apples(self):
        for n in range(0, self.settings.init_apples_amount) :
            new_apple = Apple(self)
            self.apples.add(new_apple)
     
     
    def check_events(self):
        """response to the command from mouse and keyboard"""
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
    
    
    def check_keydown(self,event):
        """check the movement state of snake_1 first"""
        if event.key == pygame.K_RIGHT:
            self.snake_1.moving_right =True
        if event.key == pygame.K_LEFT:
            self.snake_1.moving_left =  True
        if event.key == pygame.K_DOWN:
            self.snake_1.moving_down = True
        if event.key == pygame.K_UP:
            self.snake_1.moving_up = True
            
        """then check the movement state of snake_0"""
        if event.key ==pygame.K_d:
            self.snake_0.moving_right = True
        if event.key == pygame.K_a:
            self.snake_0.moving_left = True
        if event.key == pygame.K_s:
            self.snake_0.moving_down = True
        if event.key == pygame.K_w:
            self.snake_0.moving_up = True
            
    
    def check_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.snake_1.moving_right = False
        if event.key == pygame.K_LEFT:
            self.snake_1.moving_left =  False
        if event.key == pygame.K_DOWN:
            self.snake_1.moving_down = False
        if event.key == pygame.K_UP:
            self.snake_1.moving_up = False
            
        """then check the movement state of snake_0"""
        if event.key ==pygame.K_d:
            self.snake_0.moving_right = False
        if event.key == pygame.K_a:
            self.snake_0.moving_left = False
        if event.key == pygame.K_s:
            self.snake_0.moving_down = False
        if event.key == pygame.K_w:
            self.snake_0.moving_up = False
    
    
    def update_apples(self):
        if self.apples_amount < self.settings.bound_apples_amount:
            self.apples.empty()
            self.creat_apples()
        else:
            for apple in self.apples.copy():
                if apple.apple_x == self.snake_0.x and apple.apple_y == self.snake_0.y:
                    apple.remove()
                    self.snake_0.length += 1
                    self.apples_amount -=1
                elif apple.apple_x == self.snake_1.x and apple.apple_y == self.snake_1.y:
                    apple.remove()
                    self.snake_1.length += 1
                    self.apples_amount -= 1
    
    
    def cross_border(self,snake):
        """check whether this snake has crossed the border or not """
        if snake.x >self.settings.screen_length or snake.y >self.settings.screen_height:
            return True
        elif snake.x <0 or snake.y <0:
            return True
        else: 
            return False
    
    
    def check_eat_self(self,snake):    
        """check whether this snake has eaten itself"""
        for x in snake.list[:-1]:
            if x == snake.head:
                return True
        return False
    
    def mutual_smash(self, snake_0, snake_1):
        """check if these two snakes have crashed"""
        crash = False
        for x in snake_0.list[:]:
            if x == snake_1.head:
                crash = True
        for x in snake_1.list[:]:
            if x ==snake_0.head:
                crash = True    
        if crash == True:
            self.game_active = False
            if snake_0.length > snake_1.length:
                self.winner = "Player0"
            elif snake_0.length == snake_1.length:
                self.winner = "Player0 and Player1"
            else:
                self.winner = "Player1"
    
    
    def display_message(self, msg, color):
        font_style = pygame.font.SysFont(None, 50)
        message = font_style.render(msg, True, color)
        self.screen.blit(message, [self.settings.screen_length / 6, self.settings.screen_height / 3])
        pygame.display.update()
    

    def update_snake_0(self):
            if self.snake_0.moving_right :
                self.snake_0.x += self.snake_0.block
            if self.snake_0.moving_left :
                self.snake_0.x -= self.snake_0.block
            if self.snake_0.moving_down:
                self.snake_0.y += self.snake_0.block
            if self.snake_0.moving_up:
                self.snake_0.y -= self.snake_0.block
                
            self.snake_0.head = []
            self.snake_0.head.append(self.snake_0.x)
            self.snake_0.head.append(self.snake_0.y)
            self.snake_0.list.append(self.snake_0.head)
            if len(self.snake_0.list) > self.snake_0.length:
                del self.snake_0.list[0]
                
            if self.cross_border(self.snake_0) or self.check_eat_self(self.snake_0):
                self.game_active = False
                self.winner = "Player1"
    
    
    def update_snake_1(self):
            if self.snake_1.moving_right :
                self.snake_1.x += self.snake_1.block
            if self.snake_1.moving_left :
                self.snake_1.x -= self.snake_1.block
            if self.snake_1.moving_down:
                self.snake_1.y += self.snake_1.block
            if self.snake_1.moving_up:
                self.snake_1.y -= self.snake_1.block     
            
            self.snake_1.head = []
            self.snake_1.head.append(self.snake_1.x)
            self.snake_1.head.append(self.snake_1.y)
            self.snake_1.list.append(self.snake_1.head)
            if len(self.snake_1.list) > self.snake_1.length:
                del self.snake_1.list[0] 
            
            if self.cross_border(self.snake_1) or self.check_eat_self(self.snake_1):
                self.game_active = False
                self.winner = "Player0" 
    
    
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for apple in self.apples.sprites():
            apple.draw_apple()
        self.snake_0.draw_snake()
        self.snake_1.draw_snake()
        pygame.display.flip()
        
                         
    def run_game(self):
        while True:
            self.check_events()
            if self.game_active:
                self.update_apples()
                self.update_snake_0()
                self.update_snake_1()
                self.mutual_smash(self.snake_0, self.snake_1)
            if not self.game_active:
                if self.winner == "Player0":
                    message= "The final winner of this game is Player0"
                elif self.winner == "Player0 and Player1":
                    message ="The final winners of this game are Player0 and Player1"
                else:
                    message ="The final winner of this game is Player1"
                self.display_message(message,(0,0,250))    
                    
            self.update_screen()
            self.clock.tick(20)
     
 
      
ai = GreedySnakes()
ai.run_game()               
               
        