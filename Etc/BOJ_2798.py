def solution():
    _, objective = [int(num) for num in input().split(" ")]
    cards = [int(num) for num in input().split(" ")]
    result = 0

    for i in range(len(cards) - 2):
        for j in range(i + 1, len(cards) - 1):
            for k in range(j + 1, len(cards)):
                choice = cards[i] + cards[j] + cards[k]
                if choice == objective:
                    return choice
                elif choice < objective:
                    result = max(result, choice)

    return result


if __name__ == "__main__":
    print(solution())
