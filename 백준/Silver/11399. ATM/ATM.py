import sys
n = int(input())
P = list(map(int, sys.stdin.readline().split()))

P.sort() #앞 대기 시간이 줄어야 적어진다.

res = 0
for i in range(1, n+1):
    res+=sum(P[:i])
print(res)