def solution():
    words = input()
    temp_list = []
    result = ""
    tagged = 0
    for word in words:

        if word == "<":
            tagged = 1
            if temp_list:
                result += "".join(temp_list[::-1])
                temp_list = []
        elif word == " ":
            if not tagged:
                result += "".join(temp_list[::-1])
                temp_list = []

        if tagged:
            result += word
            if word == ">":
                tagged = 0
        else:
            if word == " ":
                result += " "
            else:
                temp_list.append(word)

    if temp_list:
        result += "".join(temp_list[::-1])

    return result


if __name__ == "__main__":
    res = solution()
    print(res)
