"""
2개의 stack을 활용하는 문제
"""

from collections import deque


def solution():
    result = []
    for _ in range(int(input())):
        words = input()
        stack = deque()
        temp_stack = deque()

        for word in words:
            if word == "<":
                if len(stack) != 0:
                    temp_stack.append(stack.pop())
            elif word == ">":
                if len(temp_stack) != 0:
                    stack.append(temp_stack.pop())
            elif word == "-":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(word)
        while len(temp_stack) != 0:
            stack.append(temp_stack.pop())
        result.append("".join(stack))
    return result


if __name__ == "__main__":
    result = solution()
    for i in result:
        print(i)
