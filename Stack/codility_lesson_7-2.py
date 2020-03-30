"""
https://app.codility.com/demo/results/trainingW36S74-TKP/
codility - Lesson 7 Fish
"""

from collections import deque

def solution(A, B):
    
    stack = deque()
    res = 0
    for fish in range(len(B)):
        if B[fish] == 0:
            if not stack:
                res+=1
            else:
                while stack:
                    if A[fish] > A[stack[-1]]:
                        stack.pop()
                    else:
                        break
                # upstream 물고기가 downstream을 모두 먹은 경우
                if not stack:
                    res+=1
        else:
            stack.append(fish)
    # downstream만 남은 경우
    if stack:
        res+=len(stack)
    return res