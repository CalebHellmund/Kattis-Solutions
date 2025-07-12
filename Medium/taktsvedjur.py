# Problem: Taktsveðjur
# Link: https://open.kattis.com/problems/taktsvedjur
# Difficulty: Medium 

num = int(input())
score = 0
multiply = 1
streak = 0
for i in range(num):
    n = input()
    if int(n) > 0:
        streak +=1
        if streak == multiply*2 and multiply < 8:
            multiply *=2
            streak = 0
    else:
        streak = 0
        if multiply > 1:
            multiply/=2
    score+=int(n)*int(multiply)
print(score)