"""
Lesson 4 - PermCheck
https://app.codility.com/demo/results/trainingDUUJG8-4PK/
"""

def solution(A):
    ck = [0] * (len(A)+1)
    res = 0
    for elem in A:
        # 숫자가 length보다 큰 경우는 오류
        if elem > len(A):
            return 0
        if ck[elem] == 0:
            ck[elem] = 1
        else:
            pass
        
    if sum(ck) == len(A):
        res = 1
        
    return res