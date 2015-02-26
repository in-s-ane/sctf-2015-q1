# File: o (Python 3.4)

import codecs
a = input('Input password:')
q = codecs.decode(a, 'hex')
x = 0
e = ''
for i in a:
    x *= 7
    x += 98
    l = ord(i) + x
    l %= 256
    e += chr(l)

b = open(e)
print(b.read())
b.close()
