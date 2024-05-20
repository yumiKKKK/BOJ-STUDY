import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    dic = {}
    for j in range(n):
        name, types = input().split()
        if types in dic:
            dic[types].append(name)
        else:
            dic[types] = [name]
    res=1
    for k in dic:
        res*=(len(dic[k])+1)
    print(res-1)
        

