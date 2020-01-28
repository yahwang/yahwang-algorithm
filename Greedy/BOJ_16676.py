def solution():
    earning = int(input())
    for i in range(1, 11):
        if earning < int("1" * (i + 1)):
            return i


if __name__ == "__main__":
    res = solution()
    print(res)
