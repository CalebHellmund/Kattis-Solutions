
# Problem: Simplicity
# Link: https://open.kattis.com/problems/simplicity
# Difficulty: Easy

from collections import defaultdict as dd

freq = dd(int)
a = list(input())

for letter in a:
    freq[letter] += 1

freqs = sorted(freq.values())

total = 0
while len(freqs) > 2:
    total += freqs.pop(0)

print(total)