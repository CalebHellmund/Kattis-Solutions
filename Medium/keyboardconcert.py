# Problem: Keyboards in Concert
# Link: https://open.kattis.com/problems/keyboardconcert
# Difficulty: Medium

instruments, n = map(int, input().split())
keys = []
for x in range(instruments):
    keys.append(input().split())
    keys[x] = keys[x][1:]
notes = input().split()
switch = 0

def switchKeyboard(index):
    options = []
    for x in range(instruments):
        y, worth = 0, 0
        while notes[index+y] in keys[x]:
            worth += 1
            y += 1
            if index+y == n:
                break
        options.append(worth)
    return options.index(max(options))

current = switchKeyboard(0)

for x, y in enumerate(notes):
    if y in keys[current]:
        continue
    else:
        current = switchKeyboard(x)
        switch += 1
print(switch)