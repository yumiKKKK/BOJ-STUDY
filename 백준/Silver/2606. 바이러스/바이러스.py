from collections import deque

n = int(input()) #num computers
m = int(input()) #num connected computers

g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]

def bfs(g, v, visited):
    global count
    queue = deque([1])
    visited[v] = True
    while queue:
        v = queue.popleft()
        count+=1
        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
count = 0
visited = [False]*(n+1)
bfs(g, 1, visited)
print(count-1)