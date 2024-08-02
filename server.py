import socket
import threading
import time

PORT = 1145
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((SERVER, PORT))
except socket.error as e:
    str(e)


def read_pos(string):
    string = string.split(',')
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])


pos = [(0, 0), (100, 100)]


def handle_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    print(f"[NEW CONNECTION] {player} connected.")
    reply = ''
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print('[DISCONNECTION] Disconnected.')
                break
            else:
                if player == 1:
                    reply = pos[0]
                if player == 0:
                    reply = pos[1]

                print('[RECEIVED] ', data)
                print('[SENDING] ', reply)
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print('[DISCONNECTION] Lost connection.')
    conn.close()


def start():
    server.listen(2)
    print(f"[LISTENING] The server started listening on {SERVER}")
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
