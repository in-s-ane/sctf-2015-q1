import math

x = 3466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
y = []
z = 3.14

m = "" #HIDDEN
n = ""
p = ""

def a(b):
    return not [x for x in xrange(2,int(math.sqrt(b))) if b%x == 0]
	
def c(d):
    e = xrange(2,d)
    f = 2
    while not y and f in e:
        if d%f==0 and a(f):
            y = y + [f] + c(d/f)
        f += 1

def encrypt():
    if len(y) == 0:
        c(x)

    for g in y:
        z += g
        z = math.sqrt(z)
        z *= 1.1
        z -= (g*0.1)
        z = abs(z)
	
    n = ''.join(str(ord(q)) for q in m)

    for h in n:
        if int(h) == 0:
            p = p + repr(int(z/9999))
        else:
            p = p + repr(int(z/int(h)*999))

    p = p.replace("L","_")
    p = p[:-1]
    print(p)

def decrypt(p):
    y = []
    c(x)
    p = p[:1]
    p = p.replace("_" ,"L")
    for g in y:
        z += g
        z = math.sqrt(z)
        z *= 1.1
        z -= (g * 0.1)
        z = abs(z)
    while len(p) > 0:
        index = p.find("L")
        a = float(p[0:index + 1])
