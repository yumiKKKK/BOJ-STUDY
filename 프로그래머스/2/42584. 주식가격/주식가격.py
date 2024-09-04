from collections import deque
def solution(prices):
    n = len(prices)
    p = deque(prices)
    dp = []
    while p:
        a = p.popleft()
        cnt = 0
        for i in p:
            cnt+=1
            if a > i:
                break
        dp.append(cnt)
    return dp
         