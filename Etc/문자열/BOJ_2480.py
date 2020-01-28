def solution():
    hands = input().split()
    ms_hand = hands[:2]
    tk_hand = hands[2:]

    if ms_hand[0] == ms_hand[1]:
        if ms_hand[0] == "R":
            if "P" in tk_hand:
                return "TK"
            elif tk_hand[0] == tk_hand[1] and "S" in tk_hand:
                return "MS"
        elif ms_hand[0] == "P":
            if "S" in tk_hand:
                return "TK"
            elif tk_hand[0] == tk_hand[1] and "R" in tk_hand:
                return "MS"
        elif ms_hand[0] == "S":
            if "R" in tk_hand:
                return "TK"
            elif tk_hand[0] == tk_hand[1] and "P" in tk_hand:
                return "MS"

    if tk_hand[0] == tk_hand[1]:
        if tk_hand[0] == "R":
            if "P" in ms_hand:
                return "MS"
            elif ms_hand[0] == ms_hand[1] and "S" in ms_hand:
                return "TK"
        elif tk_hand[0] == "P":
            if "S" in ms_hand:
                return "MS"
            elif ms_hand[0] == ms_hand[1] and "R" in ms_hand:
                return "TK"
        elif tk_hand[0] == "S":
            if "R" in ms_hand:
                return "MS"
            elif ms_hand[0] == ms_hand[1] and "P" in ms_hand:
                return "TK"
    return "?"


if __name__ == "__main__":
    res = solution()
    print(res)
