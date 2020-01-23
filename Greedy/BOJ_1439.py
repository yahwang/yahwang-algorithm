import sys

input = sys.stdin.readline


def solution():
    words = input().strip()
    zero_cnt = 0
    one_cnt = 0
    for idx, word in enumerate(words):
        if idx != 0 and words[idx - 1] == word:
            pass
        elif word == "1":
            one_cnt += 1
        elif word == "0":
            zero_cnt += 1
    return min(one_cnt, zero_cnt)


if __name__ == "__main__":
    res = solution()
    print(res)
