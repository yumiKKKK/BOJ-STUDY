import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    if 2*n > 9999:
        return 2*n%10000
    return 2*n

def S(n):
    if n == 0:
        return 9999
    return n-1

def L(n):
    return (10*n+(n//1000))%10000

def R(n):
    return (n//10+(n%10)*1000)%10000
    

T = int(input())
for i in range(T):
    A, B = map(int, input().strip().split())
    visited = [0 for _ in range(10001)]
    queue = deque()
    queue.append([A,''])
    visited[A] = 1
    while queue:
        n, cmd = queue.popleft()
        if n == B:
            print(cmd)
            break
        d = D(n)
        if not visited[d]:
            visited[d]=True
            queue.append([d, cmd+'D'])
        s = S(n)
        if not visited[s]:
            visited[s]=True
            queue.append([s, cmd+'S'])
        l = L(n)
        if not visited[l]:
            visited[l]=True
            queue.append([l, cmd+'L'])
        r = R(n)
        if not visited[r]:
            visited[r]=True
            queue.append([r, cmd+'R'])
    
    
