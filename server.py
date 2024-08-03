import socket
import threading
import time
import pickle
from player import Player

PORT = 10000
# SERVER = '127.0.0.1'
SERVER = socket.gethostbyname(socket.gethostname())# Get the host address e.g. SERVER -> '192.1.1.5'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((SERVER, PORT))
except socket.error as e:
    str(e)



players = [Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,255,0))]


def handle_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    print(f"[NEW CONNECTION] {player} connected.")
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print('[DISCONNECTION] Disconnected.')
                break
            else:
                if player == 1:
                    reply = players[0]
                if player == 0:
                    reply = players[1]

                print('[RECEIVED] ', data)
                print('[SENDING] ', reply)
            conn.send(pickle.dumps(reply))
        except:
            break

    print('[DISCONNECTION] Lost connection.')
    conn.close()


def start():
    server.listen(2)
    print(f"[LISTENING] The server started listening on {SERVER}:{PORT}")
    current_player = 0
    while True:
        conn, addr = server.accept()
        print('[CONNECTION] Connected to :', addr)
        thread = threading.Thread(target=handle_client, args=(conn, current_player))
        thread.start()
        current_player += 1
        # print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print('[STARTING] The server is starting...')
start()
