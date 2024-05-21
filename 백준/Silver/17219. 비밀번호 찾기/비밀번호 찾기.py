import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dic={}
for i in range(N):
    addr, pw = input().split()
    dic[addr] = pw
for i in range(M):
    print(dic[input().strip()])
    
    









