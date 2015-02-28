import sys
from hashlib import sha1

rainbow = ["red", "green", "yellow", "blue", "orange", "indigo", "violet"]

number_color = []
for num in range(1000, 10000):
    for color in rainbow:
        number_color.append("%d%s" % (num, color))

f = open('bobs_info.txt', 'r')
name = f.readline().strip()
hashed = f.readline().strip()
f.close()

f = open('cat_names.txt', 'r')

for cat_name in f:
    cat_name = cat_name.strip().lower()
    for e in number_color:
        password = cat_name + e
        if sha1(password).hexdigest() == hashed:
            f = open('password.txt', 'w')
            f.write(password)
            f.close()
            print "Bob's password: %s" % (password)
            sys.exit(0)
    print cat_name
