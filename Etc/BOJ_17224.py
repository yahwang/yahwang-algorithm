import sys

input = sys.stdin.readline


def solution():
    N, L, K = [int(i) for i in input().split()]
    problems = []
    score = 0
    for i in range(N):
        problems.append([int(i) for i in input().split()])

    problems.sort(key=lambda x: x[1], reverse=True)

    solved = []

    for quiz in problems:
        if K == 0:
            return score
        if quiz[1] <= L:
            score += 140
            solved.append(True)
            K -= 1
        else:
            solved.append(False)
            continue

    for idx, quiz in enumerate(problems):
        if K == 0:
            return score
        if solved[idx] or quiz[0] > L:
            continue
        else:
            score += 100
        K -= 1

    return score


if __name__ == "__main__":
    res = solution()
    print(res)
