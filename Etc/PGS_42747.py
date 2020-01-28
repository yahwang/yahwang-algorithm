"""
dp 활용
"""


def solution(citations):
    answer = 0
    cit_dict = {}

    for cit in citations:
        cit_dict[cit] = cit_dict.setdefault(cit, 0) + 1

    dp = [0 for _ in range(10000)]
    dp[0] = cit_dict.get(0, 0)

    for idx in range(1, 10000):
        dp[idx] = dp[idx - 1] + cit_dict.get(idx, 0)
        if len(citations) - dp[idx - 1] >= idx and dp[idx - 1] <= idx:
            answer = max(answer, idx)
    return answer
