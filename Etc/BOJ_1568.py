def solution():
    birds_len = int(input())
    idx = 0
    sing = 1
    sing_cnt = 0
    while idx <= birds_len - 1:
        if birds_len - idx < sing:
            sing = 1
        idx += sing
        sing += 1
        sing_cnt += 1
    return sing_cnt


if __name__ == "__main__":
    res = solution()
    print(res)
