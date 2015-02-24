'''
Starting at 1
bashing out the first: 131027
bashing out the second: 16814935

Starting at 0
bashing out the first: 112856
bashing out the second: 14649808
'''

def algo(num):
    iters = 0
    while iters < 100:
        palinstr = str(num)
        revPalinstr = palinstr[::-1]
        if palinstr == revPalinstr:
            return iters
        num += int(revPalinstr)
        iters += 1

count = 0
for i in range(101, 1000000):
    if algo(i) > 10:
        count += 1
print count
