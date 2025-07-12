# Problem: Which One is Larger
# Link: https://open.kattis.com/problems/whichoneislarger
# Difficulty: Medium

in1 = input()
in2 = input()
w1, w2 = float(in1), float(in2)
i1 = list(map(int, in1.split('.')))
i2 = list(map(int, in2.split('.')))
if i1[0] == i2[0] and ((w1 > w2 and i1[1] <= i2[1]) or (w1 < w2 and i1[1] >= i2[1])):
    print('-1')
else:
    print(max(w1, w2))