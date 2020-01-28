def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for idx, quiz in enumerate(answers):
        if quiz == p1[idx % 5]:
            cnt[0] += 1
        if quiz == p2[idx % 8]:
            cnt[1] += 1
        if quiz == p3[idx % 10]:
            cnt[2] += 1
    max_val = max(cnt)
    answer = [i + 1 for i in range(3) if cnt[i] == max_val]
    return answer
