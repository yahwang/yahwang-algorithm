# 비타알고 시즌3 03월 1주차 백신문제

import sys
from collections import deque

# 문제에 맞게 개수 조절
adj = [[] for _ in range(200001)]
# set으로 중복 체크
ck = set()


def bfs(p):
    # 이미 확인한 환자는 제외해서 불필요 연산 제거
    if p in ck:
        return 0

    queue = deque()
    cnt = 0
    queue.append(p)

    # 무한루프에 빠지지 않도록 ck값으로 확인
    while queue:
        p_next = queue.popleft()
        if p_next not in ck:
            ck.add(p_next)
            cnt += 1
            for i in adj[p_next]:
                queue.append(i)
    return cnt


def solution():
    input = sys.stdin.readline

    N, M = [int(i) for i in input().split()]
    for _ in range(M):
        p1, p2 = list(map(int, input().split()))
        adj[p1].append(p2)
        adj[p2].append(p1)

    res = 0
    res_p = 0

    for patient in range(1, N + 1):
        total = bfs(patient)
        if total > res:
            res = total
            res_p = patient

    print(res_p, res)


if __name__ == "__main__":
    solution()

