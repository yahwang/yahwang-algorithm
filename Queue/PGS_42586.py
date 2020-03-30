from collections import deque

def solution(progresses, speeds):
    answer = []
    finished=[]
    for idx, s in enumerate(speeds):
        cnt = (100 - progresses[idx])//s+1
        finished.append(cnt)
    
    while finished:
        published=finished.pop(0)
        completed = 1
        while finished:
            if published >= finished[0]:
                finished.pop(0)
                completed+=1
            else:
                break
        answer.append(completed)
    return answer