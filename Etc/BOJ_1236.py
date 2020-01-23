def solution():
    row, col = [int(i) for i in input().split()]
    protected_col = set()
    protected_row = set()
    for i in range(row):
        for idx, j in enumerate(input()):
            if j == "X":
                protected_row.add(i)
                protected_col.add(idx)

    col_arr = [i for i in range(col) if i not in protected_col]
    row_arr = [i for i in range(row) if i not in protected_row]
    return max(len(col_arr), len(row_arr))


if __name__ == "__main__":
    res = solution()
    print(res)
