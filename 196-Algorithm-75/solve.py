'''
bashing out the first: 113068
bashing out the second: 14652767
'''

# recursive solution
def algo(num, iters):
    if iters >= 100:
        return 0
    rev = int(str(num)[::-1])
    num += rev
    palinstr = str(num)
    if palinstr != palinstr[::-1]:
        return algo(num, iters+1)
    else:
        return iters

# looping solution
def algo2(num):
    iters = 1
    while iters < 100:
        rev = int(str(num)[::-1])
        num += rev
        palinstr = str(num)
        if palinstr == palinstr[::-1]:
            return iters
        iters += 1

#print algo2(5280) # Should return 3
count = 0
for i in range(101, 100000000):
    if algo2(i) > 10:
        count += 1
print count
