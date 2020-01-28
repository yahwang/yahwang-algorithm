"""
queue와 비슷한 풀이
"""


def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill)

    for tree in skill_trees:
        q = [i for i in skill[::-1]]

        for s in tree:
            if s in skill_set:
                if q:
                    if q[-1] == s:
                        q.pop()
                    else:
                        answer -= 1
                        break
        answer += 1

    return answer
