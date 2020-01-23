import sys

input = sys.stdin.readline


def solution():
    arr_len, pos = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    arr.sort()
    return arr[pos - 1]


if __name__ == "__main__":
    res = solution()
    print(res)
