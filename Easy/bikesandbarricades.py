# Problem: Bikes and Barricades
# Link: https://open.kattis.com/problems/bikesandbarricades
# Difficulty: Easy

d = -1
for x in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x2-x1 == 0:
        if x2 != 0:
            continue
        else:
            a = min(y1, y2)
            if a > 0 and (a < d or d == -1):
                d = a
                continue
    s = (y2-y1)/(x2-x1)
    b = y1 - x1*s
    if b > 0 and ((x1 >= 0 and x2 <=0) or (x2 >= 0 and x1 <= 0)) and (b < d or d == -1):
        d = b
print(d)