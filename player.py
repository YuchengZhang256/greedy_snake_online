import pygame

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 4

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x -= self.vel
        if key[pygame.K_d]:
            self.x += self.vel
        if key[pygame.K_w]:
            self.y -= self.vel
        if key[pygame.K_s]:
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)