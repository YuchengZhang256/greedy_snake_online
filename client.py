import socket
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Client')


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
        self.rect = (self.x, self.y, self.width, self.height)


# player = pygame.Rect((300, 250, 50, 50))

HEADER = 64
PORT = 1145
FORMAT = 'utf-8'
DISCONNECTION_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def redraw(scr, player):
    scr.fill((0, 0, 0))
    player.draw(scr)
    pygame.display.update()


def main():
    p = Player(50, 50, 100, 100, (0, 0, 255))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                send('!DISCONNECT')
        p.move()
        redraw(screen, p)

    pygame.quit()


main()
