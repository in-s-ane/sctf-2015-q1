import socket
import random


for i in range(1 , 25565):
    HOST = "python.sctf.io"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, i))
        received = sock.recv(1024)
        print received
    except:
        print "Failed on: "
        print i
    sock.close()
