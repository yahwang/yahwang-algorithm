"""
stack에 초깃값 넣어주는 거랑 stack 길이가 0일 때 주의
"""

from collections import deque


def solution(heights):
    answer = [0]
    stack = deque([(1, heights[0])])
    for idx, height in enumerate(heights[1:], start=2):
        while stack[-1][1] <= height:
            stack.pop()
            if len(stack) == 0:
                break

        if len(stack) == 0:
            answer.append(0)
        else:
            answer.append(stack[-1][0])

        stack.append((idx, height))

    return answer
