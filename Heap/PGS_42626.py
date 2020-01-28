import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        s_index = first + 2 * second
        heapq.heappush(scoville, s_index)
        answer += 1
        if scoville[0] >= K:
            return answer

    return -1
