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

for name in f:
    name = name.strip().lower()
    for e in number_color:
        password = name + e
        #print password
        if sha1(password).hexdigest() == hashed:
            print "%s's password: %s" % (name, password)
            break
    print name
