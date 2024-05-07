import sys
from collections import deque

n = int(input())
A=[]
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().rstrip())))

# n=7
# A = [[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1],[0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,0,0,0]]

cnt = []
count=0
def bfs(A, x, y, visited):
    n= len(A)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    queue = deque([(x, y)])
    A[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and A[nx][ny] ==1:
                queue.append((nx, ny))
                A[nx][ny] = 0
                count+=1
    cnt.append(count)
    
visited = [[False] * n ]* n
for i in range(n):
    for j in range(n):
        if A[i][j]==1:
            bfs(A, i, j, visited)

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
        print(cnt[i])