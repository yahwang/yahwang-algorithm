import sys

input = sys.stdin.readline


def solution():
    number = int(input())
    fib = [0] * (number + 1)
    fib[1] = 1
    for i in range(2, number + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[number]


if __name__ == "__main__":
    print(solution())
