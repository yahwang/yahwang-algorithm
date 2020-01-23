"""
난이도 중급
"""

import sys

input = sys.stdin.readline


def solution():
    _ = input()
    cranes = [int(i) for i in input().split()]
    _ = input()
    boxes = [int(i) for i in input().split()]
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    if boxes[0] > cranes[0]:
        return -1

    idx = 0
    total_time = 0
    while boxes:
        for crane in cranes:
            if len(boxes) == 0:
                break
            while idx < len(boxes):
                if crane >= boxes[idx]:
                    boxes.remove(boxes[idx])
                    break
                idx += 1
        idx = 0
        total_time += 1

    return total_time


if __name__ == "__main__":
    res = solution()
    print(res)
