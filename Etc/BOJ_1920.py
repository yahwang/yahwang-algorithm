import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    sets = set([int(i) for i in input().split()])
    M = int(input())
    for i in input().split():
        if int(i) in sets:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()
