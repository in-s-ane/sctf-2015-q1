'''
Part 1: Apply the 196-Algorithm to all numbers greater than 100 and less than one million and take the count of all the end results that take greater than 10 iterations and less than 100. The answer to Part 1 is the count.
Part 2: Redo Part 1 with all numbers greater than 100 and less than one-hundred million. The answer to Part 2 is the redone count.

Starting at original number
Part 1 solution: 131027
Part 2 solution: 16814935

Ignoring original number
Part 1 solution: 113068
Part 2 solution: 14652767
'''

def algo(num):
    iters = 1
    while iters < 100:
        palinstr = str(num)
        revPalinstr = palinstr[::-1]
        if palinstr == revPalinstr:
            return iters
        num += int(revPalinstr)
        iters += 1

count = 0
i = 101
while i < 100000000:
    if algo(i + int(str(i)[::-1])) > 10:
        count += 1
    i += 1
print count
f = open('solution.txt', 'w')
f.write(str(count))
f.close()
