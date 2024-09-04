import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    k = heapq.heappop(scoville)
    while k < K:
        try:
            new_k = k + (heapq.heappop(scoville) * 2)
        except:
            return -1
        heapq.heappush(scoville,new_k)
        k = heapq.heappop(scoville)
        answer += 1
    return answer