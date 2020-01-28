"""
효율성 테스트 2, 테스트 3 실패
MAX HEAP을 활용
"""

import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    stock_heap = []
    dates_idx = 0
    for day in range(k):
        if dates_idx < len(dates) and day == dates[dates_idx]:
            heapq.heappush(stock_heap, -supplies[dates_idx])
            dates_idx += 1
        if stock <= 0:
            while stock <= 0:
                stock -= heapq.heappop(stock_heap)
                answer += 1
        stock -= 1

    return answer


""" 
정답 ( 다른 분 풀이 참고 )
"""

import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    dates_idx = 0
    while stock < k:
        # stock은 날짜보다 항상 커야 함
        while dates_idx < len(dates) and dates[dates_idx] <= stock:
            heapq.heappush(heap, -supplies[dates_idx])
            dates_idx += 1
        stock -= heapq.heappop(heap)
        answer += 1

    return answer
