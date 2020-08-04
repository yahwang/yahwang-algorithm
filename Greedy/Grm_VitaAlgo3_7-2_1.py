# 7월 2주차 : 곱셈놀이


def solution():
    n, m = map(int, input().split())
    cnt = 0
    if m % n != 0:
        return -1

    num = m // n
    if num % 2 != 0 and num % 3 != 0:
        return -1

    while num != 1:
        if num % 3 == 0:
            num = num // 3
            cnt += 1

        if num % 2 == 0:
            num = num // 2
            cnt += 1

    return cnt


print(solution())
