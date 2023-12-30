import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        if scoville[0] < K:
            m1, m2 = heapq.heappop(scoville), heapq.heappop(scoville)
            heapq.heappush(scoville, m1 + m2 * 2)
            answer += 1
        else:
            return answer
    if scoville[0] > K:
        return answer
    return -1
