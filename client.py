import socket
import pygame
from network import Network
from player import Player
import pickle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Client')

clientNumber = 0


def redraw(scr, player, player2):
    scr.fill((0, 0, 0))
    player.draw(scr)
    player2.draw(scr)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.get_p()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2=n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw(screen, p, p2)


main()
