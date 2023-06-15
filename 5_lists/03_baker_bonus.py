# Problem name: ECOO '17 R3 P1 - Baker Brie
# Code: ecoo17r3p1
# Link: https://dmoj.ca/problem/ecoo17r3p1

for _ in range(10):
    line = input().split()
    franchisees = int(line[0])
    days = int(line[1])

    grid = []

    for _ in range(days):
        row = input().split()

        for i in range(franchisees):
            row[i] = int(row[i])
        
        grid.append(row)

    bonus = 0

    for row in grid:
        total = sum(row)
        if total % 13 == 0:
            bonus += total // 13
        
    for i in range(len(grid[0])):
        total = 0
        for j in range(len(grid)):
            total = total + grid[j][i]
        if total % 13 == 0:
            bonus += total // 13

    print(bonus)
