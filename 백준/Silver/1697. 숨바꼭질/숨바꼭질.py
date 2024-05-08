from sys import stdin
#수빈 위치, 동생 위치
N, K = map(int,stdin.readline().rstrip().split())
#방문 여부 확인
visited=[0]*(100000+1)

#bfs는 큐 자료구조를 이용 - collection모듈의 deque이용
from collections import deque
def bfs():
    #큐생성
    q=deque()
    q.append(N)
    while q:
        x=q.popleft()
        if x==K:
            print(visited[x])
            break
        for i in (x-1, x+1, 2*x):
            if 0<=i<=100000 and visited[i]==0:
                visited[i]=visited[x]+1
                q.append(i)
bfs()


