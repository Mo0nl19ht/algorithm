import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        fir = heapq.heappop(scoville)
        if not scoville:
            if fir < K:
                return -1
            return answer
        if fir >= K:
            return answer
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir+sec*2)
        answer += 1

    return answer
