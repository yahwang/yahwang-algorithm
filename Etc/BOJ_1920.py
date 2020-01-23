```
hash와 관련된 문제 ( dict 또는 set을 활용)
````

def solution():
    cnt_1 = int(input())
    array_1 = {i: int(i) for idx, i in enumerate(input().split())}
    cnt_2 = int(input())
    array_2 = [int(i) for i in input().split()]

    for number in array_2:
        if array_1.get(str(number), 0):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()
