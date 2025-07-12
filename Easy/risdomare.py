# Problem: Rice judge
# Link: https://open.kattis.com/problems/risdomare
# Difficulty: Easy
 
n = int(input())
mood = input()
options = []
for x in range(n):
    options.append(list(map(int, input().split())))
    options[x].append(options[x][0]+ options[x][1])
    options[x].append(x+1)


m = max(options, key=lambda x: x[2])[2]

comp = [x for x in options if x[2] == m]

if mood == 'antal':
    print(max(comp, key=lambda x: x[0])[3])
else:
    print(max(comp, key=lambda x: x[1])[3])