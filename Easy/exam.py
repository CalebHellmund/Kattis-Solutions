# Problem: Exam
# Link: https://open.kattis.com/problems/exam
# Difficulty: Easy

c = int(input())
yours = input()
friends = input()

same = 0
length = len(yours)
for x, y in enumerate(yours):
    if y == friends[x]:
        same += 1

if same < c:
    print(length+same-c)
else:
    print(c+length-same)