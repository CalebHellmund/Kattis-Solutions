# Problem: Neighborhood Watch
# Link: https://open.kattis.com/problems/neighborhoodwatch
# Difficulty: Medium 

def fun():
    N, K = map(int, input().split())
    if K == 0:
        print(0)
        return
    safe = []
    rating = 0
    for x in range(K):
        safe.append(int(input()))
    z = 0
    for x in range(N):
        if x + 1 == safe[z]:
            rating += (N-x)
            if z < len(safe) - 1:
                z+=1
            else:
                break
        else:
            rating += (N-safe[z]+1) 
    print(rating)
    return
fun()