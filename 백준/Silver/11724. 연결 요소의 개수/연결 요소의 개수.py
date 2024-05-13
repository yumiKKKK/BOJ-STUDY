from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(graph, x, visited):
    queue = deque([x])
    visited[x] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
visited = [False] * (n+1) 
count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count+=1
print(count)