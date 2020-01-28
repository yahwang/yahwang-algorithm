from collections import deque


def solution():
    N, K = [int(i) for i in input().split()]
    MAX = 100001
    time = [0] * MAX
    queue = deque([N])
    while queue:
        pos = queue.popleft()
        if pos == K:
            return time[pos]
        for next_pos in [pos + 1, pos - 1, pos * 2]:
            if 0 <= next_pos < MAX and time[next_pos] == 0:
                time[next_pos] = time[pos] + 1
                queue.append(next_pos)
    return 0


if __name__ == "__main__":
    res = solution()
    print(res)
