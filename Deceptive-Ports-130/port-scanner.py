import socket
import random

HOST = "python.sctf.io"

for i in range(1024, 25565):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, i))
        received = sock.recv(1024)
        if received != "":
            print received
        else:
            continue
    except:
        print "Failed on: "
        print i
    sock.close()
