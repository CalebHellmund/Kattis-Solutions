# Problem: Tree Shopping
# Link: https://open.kattis.com/problems/treeshopping
# Difficulty: Medium

n, k = map(int, input().split())

trees = [int(i) for i in input().split()]

height_diff = 101
window = trees[0:k]

counter = {}

for left in range(0, n-k+1):
    right = left + k
    if counter == {}:
        for item in trees[left:right]:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1
    else:
        first = trees[left-1]
        last = trees[right-1]

        counter[first] -= 1
        if counter[first] == 0:
            del counter[first]

        if last in counter:
            counter[last] += 1
        else:
            counter[last] = 1

    window = list(sorted(counter.keys()))
    tall = window[-1]
    short = window[0]
    height_diff = min(tall-short, height_diff)

print(height_diff)