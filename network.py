import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = '202.182.125.24'
        # self.server = '127.0.0.1'
        self.server = '36.235.130.51'
        # self.server = '0.tcp.jp.ngrok.io'
        # self.port = 1145
        # self.port = 11476
        self.port = 17720
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def get_p(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(1024))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(1024))
        except socket.error as e:
            print('network error:', e)
