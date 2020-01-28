"""
쉬운 문제
"""

import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    table = input().rstrip()
    bonus = 0
    score = 0
    for idx, ans in enumerate(table, start=1):
        if ans == "O":
            score += idx
            score += bonus
            bonus += 1
        else:
            bonus = 0
    return score


if __name__ == "__main__":
    res = solution()
    print(res)
