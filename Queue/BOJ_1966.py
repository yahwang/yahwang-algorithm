from collections import deque


def solution():
    test_case = int(input())
    results = []
    for _ in range(test_case):
        _, obj_doc = [int(i) for i in input().split()]
        docs_que = deque([(idx, int(i)) for idx, i in enumerate(input().split())])
        print_cnt = 0
        while True:
            max_priority = max(docs_que, key=lambda x: x[1])[1]
            if docs_que[0][1] == max_priority:
                print_cnt += 1
                if docs_que[0][0] == obj_doc:
                    break
                docs_que.popleft()
            else:
                docs_que.append(docs_que.popleft())
        results.append(print_cnt)

    for result in results:
        print(result)


if __name__ == "__main__":
    solution()
