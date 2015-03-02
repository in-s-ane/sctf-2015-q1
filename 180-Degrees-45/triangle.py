# Generate list of all triangular numbers (below 5050813)
f = open('triangles.txt', 'w')
i = 1
total = 0
while total < 5050813:
    total += i
    i += 1
    f.write(str(total) + '\n')
f.close()
