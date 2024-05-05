from collections import deque
import sys
 
t = int(input())
 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
def bfs(x, y, f):
    queue = deque([(x, y)])
    field[x][y] = 0
 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                queue.append((nx, ny))
                field[nx][ny] = cnt
 
 
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0] * m for _ in range(n)]
    cnt = 2
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        field[b][a] = 1
    for a in range(n):
        for b in range(m):
            if field[a][b] == 1:
                bfs(a, b, field)
                cnt += 1
    print(cnt-2)