import socket
import threading

HEADER = 64
PORT = 2024
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def start():
    server.listen()
    print(f"The {SERVER} is starting listening!")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")    
    connected = True 
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
             msg_length = int(msg_length)
             msg = conn.recv(msg_length).decode(FORMAT)
             print(f'[{addr}] {msg}')
        
        
print(f"The {SERVER} is starting now!")        
start()  