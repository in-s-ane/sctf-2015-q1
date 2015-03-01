"""This is so not gonna work, simple greedy algorithm"""

score = 0 # score counter

f = open("keelvin.txt", "r").read().split("\n")

problemList = []
worthList = []

for i in range(1, len(f)):
    data = f[i].split(" ")
    problemWorth = int(data[0])
    deduction = int(data[1])
    timeToSolve = int(data[2])
    if (problemWorth - (deduction * timeToSolve)) > 0:
        realWorth = problemWorth - (deduction * timeToSolve)
    else:
        realWorth = 0
    problemList.append([deduction, timeToSolve])
    worthList.append(realWorth)

def maxIndex(list1): # linear search that returns index
    currentMax = list1[0]
    index = 0
    for i in range(1, len(list1)):
        if list1[i] > currentMax:
            index = i
    return index

# GREEDY ALGORITHM!! <-- not gonna work

while worthList != []:
    problemNumber = maxIndex(worthList)

    score += worthList.pop(problemNumber)
    for i in range(0, len(worthList)):
        if (worthList[i] - (problemList[problemNumber][1] * problemList[i][0])) > 0:
            worthList[i] -= problemList[problemNumber][1] * problemList[i][0]
        else:
            worthList[i] = 0
    problemList.pop(problemNumber)

print score
