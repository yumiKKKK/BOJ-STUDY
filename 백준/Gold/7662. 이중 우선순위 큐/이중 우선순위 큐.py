import sys
import heapq
t = int(sys.stdin.readline())

def isEmpty(rep):
    for i in rep:
        if i[1] > 0:
            return False
    return True

for i in range(t):
    minhp = []
    maxhp = []
    rep = dict()
    k = int(sys.stdin.readline())
    
    for j in range(k):
        ch, n = sys.stdin.readline().split()
        n = int(n)
        
        if ch == 'I':
            if n in rep:
                rep[n] += 1
            else:
                rep[n] = 1
                heapq.heappush(minhp, n)
                heapq.heappush(maxhp, -n)
                
        elif ch == 'D':
            if not isEmpty(rep.items()):
                if n == 1:
                    while -maxhp[0] not in rep or rep[-maxhp[0]] < 1:
                        temp = -heapq.heappop(maxhp)
                        if temp in rep:
                            del(rep[temp])
                    rep[-maxhp[0]] -= 1
                else:
                    while minhp[0] not in rep or rep[minhp[0]] < 1:
                        temp = heapq.heappop(minhp)
                        if temp in rep:
                            del(rep[temp])
                    rep[minhp[0]] -= 1         
    if isEmpty(rep.items()):
        print('EMPTY')
    else:
        while minhp[0] not in rep or rep[minhp[0]] < 1:
            heapq.heappop(minhp)
        while -maxhp[0] not in rep or rep[-maxhp[0]] < 1:
            heapq.heappop(maxhp)
        print(-maxhp[0], minhp[0])