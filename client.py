import socket
import pygame
from network import Network

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Client')

clientNumber = 0


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

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


def read_pos(string):
    string = string.split(',')
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])


# player = pygame.Rect((300, 250, 50, 50))
#
# HEADER = 64
# PORT = 1145
# FORMAT = 'utf-8'
# DISCONNECTION_MESSAGE = '!DISCONNECT'
# SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER, PORT)
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)
# def send(msg):
#     message = msg.encode(FORMAT)
#     msg_length = len(message)
#     send_length = str(msg_length).encode(FORMAT)
#     send_length += b' ' * (HEADER - len(send_length))
#     client.send(send_length)
#     client.send(message)


def redraw(scr, player, player2):
    scr.fill((0, 0, 0))
    player.draw(scr)
    player2.draw(scr)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = Player(200, 200, 100, 100, (0, 0, 255))
    p2 = Player(20, 20, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        print(n.send(make_pos((p.x, p.y))))
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw(screen, p, p2)


main()
