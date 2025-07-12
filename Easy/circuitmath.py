# Problem: Circuit Math
# Link: https://open.kattis.com/problems/circuitmath
# Difficulty: Easy

n = int(input())

tf = input().split()

ops = input().split()
for i in range(len(ops)):
    if ops[i].isalpha():
        index = ord(ops[i]) - ord('A')
        ops[i] =( tf[index] == 'T')


# print(*ops)

while len(ops) > 1:
    # print(ops)
    for i in range(len(ops) - 2): # *
        # print(ops, 1)
        a = ops[i]
        b = ops[i+1]
        c = ops[i+2]

        if type(a)==bool and type(b)==bool and c == "*":
            ops = ops[:i] + [a and b] + ops[i+3:]
            break
            
    for i in range(len(ops) - 2): # +
        a = ops[i]
        b = ops[i+1]
        c = ops[i+2]
        if type(a)==bool and type(b)==bool and c == "+":
            ops = ops[:i] + [a or b] + ops[i+3:]
            break
    for i in range(len(ops) - 1): # -
        a = ops[i]
        b = ops[i+1]
        if type(a)==bool and b == "-":
            ops = ops[:i] + [not a] + ops[i+2:]
            break

print('T' if ops[0] else 'F')