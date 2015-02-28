from hashlib import sha1

rainbow = ["red", "green", "yellow", "blue", "orange", "indigo", "violet"]

f = open('bobs_info.txt', 'r')
name = f.readline().strip()
hashed = f.readline().strip()
f.close()

f = open('cat_names.txt', 'r')

for name in f:
    name = name.strip().lower()
    for num in range(0, 10000):
        for color in rainbow:
            password = "%s%04d%s" % (name, num, color)
            #print password
            if sha1(password).hexdigest() == hashed:
                print "%s's password: %s" % (name, password)
                break
    print name
