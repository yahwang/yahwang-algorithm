def solution(participant, completion):
    part_dict = {}
    comp_dict = {}
    answer = ""
    for person in participant:
        part_dict.setdefault(person, 0)
        part_dict[person] += 1

    for person in completion:
        comp_dict.setdefault(person, 0)
        comp_dict[person] += 1

    for person in part_dict:
        if part_dict[person] != comp_dict.get(person, 0):
            answer = person
            break

    return answer
