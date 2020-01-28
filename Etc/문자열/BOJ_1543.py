"""
간단한 탐색 문제
"""


def solution():
    words = input()
    obj_word = input()
    word_len = len(obj_word)
    idx = 0
    word_cnt = 0
    while idx <= len(words) - word_len:
        if words[idx : idx + word_len] == obj_word:
            word_cnt += 1
            idx += word_len
        else:
            idx += 1
    return word_cnt


if __name__ == "__main__":
    res = solution()
    print(res)
