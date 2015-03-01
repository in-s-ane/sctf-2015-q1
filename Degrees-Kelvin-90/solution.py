import sys, copy

f = open(sys.argv[1], "r").read().split("\n")
f = filter(None, f)
#print f

SCORE = 0 # score counter
problemList = []

for i in range(1, len(f)):
    data = f[i].split(" ")
    problemWorth = int(data[0])
    deduction = int(data[1])
    timeToSolve = int(data[2])
    # Only put problems that are still worth points after Kelvin solves it
    if (problemWorth - (deduction * timeToSolve)) > 0:
        realWorth = problemWorth - (deduction * timeToSolve)
        problemList.append([realWorth, deduction, timeToSolve])

def maxIndex(list1): # linear search that returns index
    currentMax = list1[0]
    index = 0
    for i in range(1, len(list1)):
        if list1[i] > currentMax:
            index = i
            currentMax = list1[i]
    return index if currentMax != 0 else -1

# HIGHLY INEFFICIENT BRUTE FORCE. CRINGE. WORTHY. O(N!) is NOT a good runtime.

def isZero(input_list):
    for i in input_list:
        if i != 0:
            return False
    return True

def solve(problems):
    if not isZero(problems):
        for i in range(0, len(problems)):
            problems_copy = copy.deepcopy(problems)
            problem = problems_copy.pop(i)
            for j in range(0, len(problems_copy)):
                problems_copy[j][0] -= (problem[2] * problems_copy[j][1])
                if problems_copy[j][0] < 0:
                    problems_copy[j][0] = 0
            return problem[0] + solve(problems_copy)
    return 0

for i in range(0, len(problemList)):
    problems_copy = copy.deepcopy(problemList)
    problem = problems_copy.pop(i)
    for j in range(0, len(problems_copy)):
        problems_copy[j][0] -= problem[2] * problems_copy[j][1]
        if problems_copy[j][0] < 0:
            problems_copy[j][0] = 0
    total = problem[0] + solve(problems_copy)
    if total > SCORE:
        SCORE = total
    print i

print SCORE
