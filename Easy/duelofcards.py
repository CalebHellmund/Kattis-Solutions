# Problem: Duel of Cards
# Link: https://open.kattis.com/problems/duelofcards
# Difficulty: Easy

y = []
z = []
n = int(input())
for x in range(n):
    y.append(int(input()))

for x in range(2*n):
    if x+1 not in y:
        z.append(x+1)
y = sorted(y)
z = sorted(z)
min = n
max = 0
used = []
used2 = []
for a in y[::-1]:
    for b in z:
        if b > a and b not in used:
            used.append(b)
            min -= 1
            break
for a in z[::-1]:
    for b in y:
        if b > a and b not in used2:
            used2.append(b)
            max += 1
            break

print(f"{min} {max}")