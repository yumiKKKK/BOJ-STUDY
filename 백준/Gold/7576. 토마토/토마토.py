from collections import deque
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(n)]

res=0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
queue = deque([])
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny]==0:
                queue.append((nx, ny))
                tomato[nx][ny]=tomato[x][y]+1
                
        
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append([i, j])
bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    res = max(res, max(i))
print(res-1)