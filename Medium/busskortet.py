# Problem: The Bus Card
# Link: https://open.kattis.com/problems/busskortet
# Difficulty: Medium

cost = int(input())
count = 0
while cost > 0:
    if cost >= 400:
        cost -= 500
    elif cost > 100:
        cost -= 200
    else:
        cost -= 100
    count += 1
print(count)