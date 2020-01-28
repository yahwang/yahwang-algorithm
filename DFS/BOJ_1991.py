"""
setrecursionlimit을 설정해야 한다.
방향벡터와 T/F 체크 리스트가 없는 버전
"""

import sys

sys.setrecursionlimit(10000)


def up_down_left_right(land, row, col):
    if row - 1 >= 0 and land[row - 1][col] == 1:
        land[row - 1][col] = 0
        up_down_left_right(land, row - 1, col)
    if row + 1 <= len(land) - 1 and land[row + 1][col] == 1:
        land[row + 1][col] = 0
        up_down_left_right(land, row + 1, col)
    if col - 1 >= 0 and land[row][col - 1] == 1:
        land[row][col - 1] = 0
        up_down_left_right(land, row, col - 1)
    if col + 1 <= len(land[0]) - 1 and land[row][col + 1] == 1:
        land[row][col + 1] = 0
        up_down_left_right(land, row, col + 1)


def solution():
    M, N, K = [int(i) for i in input().split()]
    land = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        col, row = [int(i) for i in input().split()]
        land[row][col] = 1
    cnt = 0
    for row in range(N):
        for col in range(M):
            if land[row][col] == 1:
                up_down_left_right(land, row, col)
                cnt += 1
    return cnt


if __name__ == "__main__":
    for i in range(int(input())):
        res = solution()
        print(res)
