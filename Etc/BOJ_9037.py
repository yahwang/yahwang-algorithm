"""
모든 숫자가 같다는 조건 설정에 주의
"""


def solution():
    child_num = int(input())
    child_arr = [int(i) for i in input().split()]

    # odd change to even
    child_arr = [i if i % 2 == 0 else i + 1 for i in child_arr]
    cnt = 0
    while len(set(child_arr)) != 1:
        # half candy and add
        child_arr = [i // 2 for i in child_arr]
        add_candy = child_arr[-1:] + child_arr[:-1]
        child_arr = [i + j for i, j in zip(child_arr, add_candy)]
        # odd change to even
        child_arr = [i if i % 2 == 0 else i + 1 for i in child_arr]
        cnt += 1
    print(cnt)


for _ in range(int(input())):
    solution()
