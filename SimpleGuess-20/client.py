import socket

HOST = "python.sctf.io"
PORT = 11234

while (True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    secret = 1
    sock.sendall(str(secret));
    received = sock.recv(1024)
    if received != "Nope!" and received != "What is your guess?":
        print received
        break

sock.close()
