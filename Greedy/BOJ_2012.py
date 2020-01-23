import sys

input = sys.stdin.readline


def solution():
    ranking = []
    diff = 0
    for _ in range(int(input())):
        ranking.append(int(input()))

    ranking.sort()

    for idx, number in enumerate(ranking, start=1):
        diff += abs(idx - number)
    return diff


if __name__ == "__main__":
    res = solution()
    print(res)
