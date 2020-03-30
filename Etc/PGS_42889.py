"""
https://programmers.co.kr/learn/courses/30/lessons/42889
"""

def solution(N, stages):
    answer = []
    on_stage = {i:0 for i in range(N+2)}
    
    for user in stages:
        on_stage[user]+=1
    cleared = len(stages)        
    for i in range(1,N+1):
        # 0으로 나누는 경우 주의
        if cleared==0:
            failure = 0
        else:
            failure = on_stage[i]/cleared
        answer.append([i,failure])
        cleared-=on_stage[i]
    answer.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer