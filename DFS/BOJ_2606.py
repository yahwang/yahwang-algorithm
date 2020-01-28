def dfs(net, ck, com):
    cnt = 1
    ck[com] = True
    for i in net[com]:
        if not ck[i]:
            cnt += dfs(net, ck, i)
    return cnt


def solution():
    N = int(input())
    L = int(input())
    net = [[] for _ in range(N + 1)]
    ck = [False for i in range(N + 1)]
    for _ in range(L):
        a, b = [int(i) for i in input().split()]
        net[a].append(b)
        net[b].append(a)
    return dfs(net, ck, 1)


if __name__ == "__main__":
    res = solution()
    print(res - 1)
