import socket
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
player = pygame.Rect((300,250,50,50))


HEADER = 64
PORT = 1145
FORMAT = 'utf-8'
DISCONNECTION_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR) 

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,0,255),player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            send('!DISCONNECT')
    pygame.display.update()

pygame.quit()