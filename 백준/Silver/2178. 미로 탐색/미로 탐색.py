import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze=[]
for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip()))) #공백없이 입력


def bfs(maze, x, y, visited):
    #상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    #queue
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1
    print(maze[n-1][m-1])
    
visited = [[False] * m ]* n
x, y = 0, 0
bfs(maze, x, y, visited)