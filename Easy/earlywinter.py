# Problem: Early Winter
# Link: https://open.kattis.com/problems/earlywinter
# Difficulty: Easy

n, d = map(int, input().split())
nums = list(map(int, input().split()))
num = 0
ever = False
for x in nums:
    if x > d:
        num += 1
    else:
        ever = True
        break
        
if ever:
    print(f"It hadn't snowed this early in {num} years!")
else:
    print("It had never snowed this early!")