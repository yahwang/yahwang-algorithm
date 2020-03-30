"""
https://app.codility.com/demo/results/trainingHSENBH-PNW/
Lesson 7 - Brackets
"""

from collections import deque

def solution(S):
    brackets={'(':')','[':']','{':'}'}
    
    stack = deque()
    
    for bracket in S:
        if bracket in brackets.keys():
            stack.append(bracket)
        else:
            if not stack:
                return 0
            if brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                return 0
    
    if stack:
        return 0
        
    return 1