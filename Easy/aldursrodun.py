# Problem: Aldursröðun
# Link: https://open.kattis.com/problems/aldursrodun
# Difficulty: Easy

kids = input()
ages = input().split()
solution = ages
import math as M
def test(solution):
    for x in range(len(solution)-1):
        if M.gcd(int(solution[x]), int(solution[x+1])) > 1:
            continue
        else:
            return False
    return True

def options(ages):
    if len(ages) > 1:
        for x in range(len(ages)):
            first = [ages[x]]
            remaining = ages[:x] + ages[x+1:]
            for y in options(remaining):
                yield first + y
    else:
        yield ages

for x in list(options(ages)):
    if test(x):
        solution = x
        break
    
if test(solution):
    print(*solution, sep=' ')
else:
    print("Neibb")