"""
계수정렬 문제
데이터 수는 매우 많지만 가능한 데이터 범위가 작은 경우
"""

import sys

input = sys.stdin.readline


def solution():
    num_arr = [0 for i in range(10001)]
    for _ in range(int(input())):
        number = int(input())
        num_arr[number] += 1
    return num_arr


if __name__ == "__main__":
    res = solution()

    for i in range(10001):
        if res[i] != 0:
            for _ in range(res[i]):
                print(i)
