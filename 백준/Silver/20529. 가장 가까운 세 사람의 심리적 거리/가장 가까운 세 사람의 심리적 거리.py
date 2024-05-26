from itertools import combinations
import sys
input = sys.stdin.readline

def mbti_dist(a, b):
    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    return dist

T = int(input())
for _ in range(T):
    N = int(input())
    mbti = input().rstrip().split()
    
    if N > 32:
        print(0)
    else:
        res = 13    
        case = combinations(mbti, 3)   
        for a, b, c in case:
            dist = 0
            dist += mbti_dist(a, b)
            dist += mbti_dist(b, c)
            dist += mbti_dist(a, c)
            
            res = min(res, dist)
        print(res)