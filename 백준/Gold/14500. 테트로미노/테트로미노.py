import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = -1

def DFS(num, x, y, total):
    global answer
    if num == 4:
        answer = max(answer, total)
    elif (total+max_value*(4-num)) <= answer: #최대값 갱신 X
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if num == 2: 
                    DFS(num+1, x, y, total+paper[nx][ny])
                DFS(num+1, nx, ny, total+paper[nx][ny])
                visited[nx][ny] = 0

visited = [[0]*M for _ in range(N)]
max_value = max(map(max, paper)) 
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(1, i, j, paper[i][j])
        visited[i][j] = 0
print(answer)