import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
    
visited = [[-1]*m for _ in range(n)]
dx, dy = [0,0,1,-1], [1,-1,0,0]

def bfs(x, y):
    queue= deque()
    queue.append((x, y))
    visited[x][y]=0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                if g[nx][ny]==0:
                    visited[nx][ny]=0
                if g[nx][ny]==1:
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx, ny))
                

for i in range(n):
    for j in range(m):
        if g[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()