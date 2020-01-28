def solution(phone_book):
    answer = True
    phone_list = []
    phone_book.sort(key=lambda x: len(x))
    for number in phone_book:
        for phone in phone_list:
            if phone == number[: len(phone)]:
                return False
        phone_list.append(number)
    return answer
