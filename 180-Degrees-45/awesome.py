'''
A triangular number is one that can be expressed in the form 1+2+3+...+n for
some positive integer n. A number is called *awesome* if it can be expressed as
the sum of two distinct triangular numbers. For example, 9 is awesome because
9=3+6, but 12 is not awesome because it cannot be expressed in that form (note
that 12=6+6 is invalid because 6,6 are not distinct). How many of the given
integers are awesome?

Input format:
The first line consists of a number k, the number of given integers. The second
line consists of k space-separated integers. It is guaranteed that these k
integers are listed in increasing order.

Output format:
A single integer, the number of the k integers that can be written as the sum of
two distinct integers.
'''

# Warning: duct-tape code below
from bisect import bisect_left
triangulars = []

def binary_search(l, x, lo=0, hi=None):
    hi = hi if hi is not None else len(l)
    pos = bisect_left(l,x,lo,hi)
    return (pos if pos != hi and l[pos] == x else -1)

# Load all the triangular numbers into memory
count = 0
a = open('triangles.txt', 'r') # List of all triangular numbers
lines = a.readlines()
for line in lines:
    triangulars.append(int(line))

f = open('triangle.txt', 'r') # Input file
lines = f.readlines()
for line in lines:
    line = line.split(' ')
    for num in line:
        try:
            num = int(num)
            for triangle in triangulars:
                if num > triangle and num != 2 * triangle and binary_search(triangulars, (num - triangle)) > -1:
                    count += 1
                    break
        except:
            pass
f.close()
print count
'''
>> python awesome.py
37894
'''
