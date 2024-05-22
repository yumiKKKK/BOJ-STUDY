import sys
T = int(input())

def func(M, N, x, y):
    while x <= M*N: # 최소공배수가 마지막이니까
        if (x-y)%N==0: # (k-x)%m=(k-y)%n=0이므로
            return x 
        x+=M
    return -1
        
for i in range(T):
    M, N, x, y = map(int,input().split())
    print(func(M, N, x, y))