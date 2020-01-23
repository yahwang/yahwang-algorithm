import sys

input = sys.stdin.readline


def solution():
    num = int(input())
    books = {}
    for _ in range(num):
        title = input().strip()
        if books.get(title, 0):
            books[title] += 1
        else:
            books[title] = 1
    max_sell = max(books.values())
    best_books = [key for key, val in books.items() if val == max_sell]
    return sorted(best_books)


if __name__ == "__main__":
    res = solution()
    print(res[0])
