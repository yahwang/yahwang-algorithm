def solution(budgets, M):
    answer = 0
    start = 1
    end = max(budgets)

    if sum(budgets) < M:
        return end

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for budget in budgets:
            if budget >= mid:
                total += mid
            else:
                total += budget
        if total == M:
            return mid
        elif total > M:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer
