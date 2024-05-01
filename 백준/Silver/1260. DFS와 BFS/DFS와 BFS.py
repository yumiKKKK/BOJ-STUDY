import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

#graph
g = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    g[n1].append(n2)
    g[n2].append(n1)
    g[n1].sort()
    g[n2].sort()

#dfs
def dfs(n, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in g[v]:
        if not visited[i]:
            dfs(n, i, visited)
    
    
#bfs
def bfs(n, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        k = queue.popleft()
        print(k, end=" ")
        for i in g[k]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(n, v, visited)
print()
visited = [False] * (n+1)
bfs(n, v, visited)