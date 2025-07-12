# Problem: Traffic Lights
# Link: https://open.kattis.com/problems/trafficlights
# Difficulty: Medium

on=[]
found=False
lights=[]
n=int(input())
for x in range(n):
    y=list(map(int,input().split()))
    y.append(y[0]+y[1])
    lights.append(y)
    on.append(0)
s=1
while not found:
    for y,x in enumerate(lights):
        if s%x[2]==0 or s%x[2]>x[0]:
            on[y]=1
        else:
            on[y]=0
    if sum(on)==n:
        found=True
        print(s-1)
    else:
        s+=1