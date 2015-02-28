import codecs
import socket
import sys
from threading import *

HOST = ''
PORT = 25566

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('SOCKET CREATED')
try:
	s.bind((HOST,PORT))
except socket.error as msg:
	print('BIND FAILED')
	sys.exit()

print('BIND COMPLETE')
s.listen(10)
print('LISTENING')

def clientthread(conn):
	try:
		conn.send(bytes("Input password:","UTF-8"))
		a = conn.recv(1024).decode("UTF-8").rstrip()
		q = codecs.decode(a,"hex")
		x = 0
		e = ""
		for i in q:
			x*=7
			x+=98
			l = i+x
			l%=256
			e+= chr(l)
		b = open(e)
		conn.send(bytes(b.read(),"UTF-8"))
		b.close()
	except Exception as abc:
		conn.send(bytes(str(abc),"UTF-8"))
		conn.close()
	conn.close()

while 1:
	conn, addr = s.accept()
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	Thread(target=clientthread,args=(conn,)).start()

s.close()
