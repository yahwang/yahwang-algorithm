"""
https://programmers.co.kr/learn/courses/30/lessons/17682
"""

def solution(dartResult):
    answer = 0
    area={'S':1,'D':2,'T':3}
    score=[]
    num=''
    for letter in dartResult:
        if letter in area.keys():
            score.append(int(num))
            num=''
            score[-1] = score[-1]**area[letter]
        elif letter == '*':
            if len(score)==1:
                score[0] = score[0]*2
            else:
                score[-1] = score[-1]*2
                score[-2] = score[-2]*2
        elif letter == '#':
            score[-1] = score[-1]*(-1)
        else:
            num+=letter
    answer += sum(score)     
    return answer