import socket

HOST = "python.sctf.io"

def guess():
    while (True):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        received = sock.recv(1024)
        print received
        secret = 9
        sock.sendall(str(secret));
        received = sock.recv(1024)
        print received
        if received != "Nope!" and received != "What is your guess?":
            break
        sock.close()

# Simple Guessing Game: qqq12345
PORT = 11234
guess()
print "------------------------"

# Not-So-Simple Guessing Game: nopeisacoolword
PORT = 11235
guess()

#
