# Problem: A Different Problem
# Link: https://open.kattis.com/problems/different
# Difficulty: Easy

while True:
     try:
         n, n2 = input().split()
         print(abs(int(n)-int(n2)))
     except:
         break