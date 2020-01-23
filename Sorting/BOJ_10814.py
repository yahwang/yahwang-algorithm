def solution():
    num = int(input())
    members = []
    for _ in range(num):
        age, name = input().split()
        members.append((int(age), name))

    for member in sorted(members, key=lambda x: x[0]):
        print(f"{member[0]} {member[1]}")


if __name__ == "__main__":
    solution()
