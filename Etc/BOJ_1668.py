import sys

input = sys.stdin.readline


def solution():
    num = int(input())
    things = []
    res = []
    for _ in range(num):
        things.append(int(input()))

    cnt = 0
    max_val = 0

    for thing in things:
        if thing > max_val:
            max_val = thing
            cnt += 1
    res.append(cnt)

    max_val = 0
    cnt = 0

    for thing in things[::-1]:
        if thing > max_val:
            max_val = thing
            cnt += 1
    res.append(cnt)
    return res


if __name__ == "__main__":
    res = solution()
    for i in res:
        print(i)
