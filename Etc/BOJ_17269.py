import sys

input = sys.stdin.readline


def solution():
    ONE, TWO = [int(i) for i in input().split()]
    name_one, name_two = input().split()
    matching = []
    letters = {
        "A": 3,
        "B": 2,
        "C": 1,
        "D": 2,
        "E": 4,
        "F": 3,
        "G": 1,
        "H": 3,
        "I": 1,
        "J": 1,
        "K": 3,
        "L": 1,
        "M": 3,
        "N": 2,
        "O": 1,
        "P": 2,
        "Q": 2,
        "R": 2,
        "S": 1,
        "T": 2,
        "U": 1,
        "V": 1,
        "W": 1,
        "X": 2,
        "Y": 2,
        "Z": 1,
    }

    for idx in range(min(ONE, TWO)):
        matching.append(name_one[idx])
        matching.append(name_two[idx])

    if ONE > TWO:
        matching.extend(name_one[idx + 1 :])
    else:
        matching.extend(name_two[idx + 1 :])

    matched = [letters[i] for i in matching]
    checked = []

    while len(matched) != 2:
        for idx in range(len(matched) - 1):
            value = (matched[idx] + matched[idx + 1]) % 10
            checked.append(value)
        matched = checked
        checked = []
    return matched


if __name__ == "__main__":
    res = solution()
    if res[0]:
        print(f"{str(res[0])}{str(res[1])}%")
    else:
        print(f"{str(res[1])}%")
