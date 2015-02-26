import sys, socket, random, itertools

HOST = "python.sctf.io"
PORT = 25565

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

received = sock.recv(1024)
print received
sock.sendall("\n")
received = sock.recv(1024)
print received
received = sock.recv(1024)
print received

choices = ["k", "j", "j", "k", "w"]

for action in itertools.cycle(choices):
    #action = raw_input("> ")
    action = action.strip()
    if action != "":
        sock.sendall(action)
        received = sock.recv(1024)
        print received
        if received != "Please do a valid action!":
            received = sock.recv(1024)
            print received

sock.close()
