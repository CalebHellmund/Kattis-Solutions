# Problem: Math Homework
# Link: https://open.kattis.com/problems/mathhomework
# Difficulty: Easy

import math as M
a, b, c, goal = map(int, input().split())
impossible = True
for x in range(M.floor(goal/a)+1):
    for y in range(M.floor(goal/b)+1):
        for z in range(M.floor(goal/c)+1):
            if x*a + y*b + z*c == goal:
                print(f"{x} {y} {z}")
                impossible = False
if impossible:
    print("impossible")