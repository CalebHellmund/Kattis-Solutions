# Problem: Digit Sum
# Link: https://open.kattis.com/problems/digitsum
# Difficulty: Hard


for x in range(int(input())):
    num = 0
    digit = 0
    min, max = input().split()
    for y, x in enumerate(max):
        if y == len(max)-1:
            x = int(x)
            while x > 0:
                num += digit + x
                x-=1
        else:
            num += int(x) * 45 * (10**(len(max)-y-2)) * (len(max)-1-y) + int(x) + int(x) * digit * 10**(len(max)-y-1)
            digit += int(x)
            x = int(x)-1
            while x >= 0:
                num += x*(10**(len(max)-1-y))
                x -=1
    digit2 = 0
    if int(min) > 0:
        min = str(int(min)-1)
    for y, x in enumerate(min):
        if y == len(min)-1:
            x = int(x)
            while x > 0:
                num -= (digit2 + x)
                x-=1
        else:
            num -= int(x) * 45 * (10**(len(min)-2-y)) * (len(min)-1-y) + int(x) + int(x) * digit2 * 10**(len(min)-y-1)
            digit2 += int(x)
            x = int(x)-1
            while x >= 0:
                num -= x*(10**(len(min)-1-y))
                x -=1
    
    print(num)