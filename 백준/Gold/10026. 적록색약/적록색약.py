import sys
from collections import deque 
input = sys.stdin.readline
n = int(input())
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    colour = a[x][y]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                if a[nx][ny] == colour:
                    queue.append((nx, ny))
                    visited[nx][ny]=True


a = [list(input().rstrip()) for _ in range(n)]

visited = [[False]*n for i in range(n)]
count=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            bfs(i, j, visited)
            count+=1

for i in range(n):
    for j in range(n):
        if a[i][j] == "R":
            a[i][j] = "G"

visited = [[False]*n for i in range(n)]
count2=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            bfs(i, j, visited)
            count2+=1

print(count, count2)