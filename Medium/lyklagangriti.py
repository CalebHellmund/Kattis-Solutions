# Problem: Lyklagangriti
# Link: https://open.kattis.com/problems/lyklagangriti
# Difficulty: Medium

outputLeft, outputRight = [], []
for x in input():
    if x == "L":
        outputRight.append(outputLeft.pop())
    elif x == "R":
        outputLeft.append(outputRight.pop())
    elif x == "B":
        outputLeft.pop()
    else:
        outputLeft.append(x)

print(''.join(outputLeft+outputRight[::-1]))