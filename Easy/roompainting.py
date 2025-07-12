# Problem: Room Painting
# Link: https://open.kattis.com/problems/roompainting
# Difficulty: Easy

def search(arr, x):
    l = 0
    r = len(arr) - 1
    best = -1
    while l <= r:
        mid = l + (r-l) //2 
        if arr[mid] >= x:
            best = mid
            r = mid -1
        else:
            l = mid + 1
    return arr[best]


n, m = map(int, input().split())

buckets = [int(input()) for _ in range(n)]

paints = [int(input()) for _ in range(m)]

excess = 0
buckets.sort()
for paint in paints:
    #bestSize = float('inf') #very very large number

    bestSize = search(buckets, paint)
    excess += bestSize - paint

print(excess)