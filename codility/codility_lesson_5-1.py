"""
Lesson 5 - CountDiv
https://app.codility.com/demo/results/trainingJN6CFU-23T/
"""

def solution(A, B, K):
    # 최소값은 나머지가 생길 경우 +1 처리 필요
    if A % K == 0:
        min_num = A // K
    else:
        min_num = A // K + 1

    max_num = B // K
    return max_num-min_num+1