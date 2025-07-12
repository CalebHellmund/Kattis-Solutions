# Problem: Gears and Axles
# Link: https://open.kattis.com/problems/gearsandaxles
# Difficulty: Medium

import math as M
gears = []
n = int(input())
for x in range(n):
    gears.append(list(map(int, input().split())))
gears = sorted(gears)
if len(gears) > 0:
    past = gears[0][0]
gearsN = []
A = []
for x in range(n):
    if past == gears[x][0]:
        A.append(gears[x][1])
    else:
        gearsN.append(A)
        A = []
        A.append(gears[x][1])
        past = gears[x][0]
gearsN.append(A)



s = 0
for x in range(len(gearsN)):
    if len(gearsN[x]) % 2 == 1:
        gearsN[x].pop(M.floor(len(gearsN[x])/2))
    for y, z in enumerate(gearsN[x]):
        if y*2 < len(gearsN[x]):
            s -= M.log(z)
        else:
            s += M.log(z)
print(s)