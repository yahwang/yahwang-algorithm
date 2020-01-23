def solution():
    num = int(input())
    points = []
    for _ in range(num):
        coord = [int(i) for i in input().split()]
        points.append((coord[0], coord[1]))
    points.sort(key=lambda x: (x[0], x[1]))
    for point in points:
        print(point[0], point[1])


if __name__ == "__main__":
    solution()
