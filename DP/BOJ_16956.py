"
DP 방식과 약간 다른 밑에서부터 업데이트하며 계산하는 방식
"
def solution():
    N = int(input())
    nums = [[int(i) for i in input().split()] for _ in range(N)]
    max_val = nums[N - 1]
    for level in range(N - 2, -1, -1):
        for idx, val in enumerate(nums[level]):
            max_val[idx] = nums[level][idx] + max(max_val[idx], max_val[idx + 1])
    return max_val[0]


if __name__ == "__main__":
    res = solution()
    print(res)
