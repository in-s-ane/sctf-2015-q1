import socket
import random

HOST = "python.sctf.io"
PORT = 11234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while (True):
    random.seed()
    secret = random.randint(1 , 11)
    sock.sendall(str(secret));
    received = sock.recv(1024)
    if received != "Nope!" or received != "What's your guess?" :
        print received
        break

sock.close()
