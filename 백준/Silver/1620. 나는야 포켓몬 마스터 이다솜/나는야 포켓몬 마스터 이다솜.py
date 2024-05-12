import sys
input = sys.stdin.readline
n, m = map(int, input().split())
names = {}
for i in range(1, n+1):
    a = input().rstrip()
    names[i] = a
    names[a] = i
    
    
for i in range(m):
    x = input().rstrip()
    if x[0].isalpha():
        print(names[x])
    else:
        print(names[int(x)])