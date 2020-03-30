"""
https://programmers.co.kr/learn/courses/30/lessons/42888
"""

def solution(record):
    answer = []
    msg_code={'Enter':'님이 들어왔습니다.','Leave':'님이 나갔습니다.'}
    user_info={}
    orders=[]
    for msg in record:
        code, *user = msg.split()
        uid = user[0]
        if code == 'Change':
            user_info[uid]=user[1]
        elif code == 'Enter':            
            user_info[uid]=user[1]
            orders.append([uid,code])
        else:
            orders.append([uid,code])
    for order in orders:
        answer.append(user_info[order[0]]+msg_code[order[1]])
    return answer