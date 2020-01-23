"""
풀었지만 비효율적인 코드(시간이 오래 걸림)
"""

from collections import deque


def solution():
    count = int(input())
    res_array = [int(input()) for _ in range(count)]
    numbers = list(range(1, count + 1))
    stack = deque()
    orders = []

    # 1-N까지 stack에 다 들어가도록 만든다.
    while numbers:
        if len(stack) == 0 or stack[-1] != res_array[0]:
            stack.append(numbers.pop(0))
            orders.append("+")
        elif stack[-1] == res_array[0]:
            stack.pop()
            res_array.pop(0)
            orders.append("-")

    # 마지막은 pop만 수행하면서 일치하는 지 확인
    while stack:
        if stack[-1] != res_array[0]:
            return []
        else:
            stack.pop()
            res_array.pop(0)
            orders.append("-")

    return "\n".join(orders)


if __name__ == "__main__":
    result = solution()
    if result:
        print(result)
    else:
        print("NO")
