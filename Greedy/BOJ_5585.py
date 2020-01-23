def solution():
    money = 1000 - int(input())
    cnt = 0
    for i in [500, 100, 50, 10, 5, 1]:
        cnt += money // i
        money = money % i
    return cnt


if __name__ == "__main__":
    res = solution()
    print(res)
