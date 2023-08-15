# Problem name: DMOPC '17 Contest 1 P1 - Fujō Neko
# Code: dmopc17c1p1
# Link: https://dmoj.ca/problem/dmopc17c1p1


# Fast input/output
import sys
input = sys.stdin.readline

# import sys
# all_data = sys.stdin.read().split('\n')

R, C = [int(x) for x in input().split()]
# print(R, C)

rows_where_X = set()
columns_where_X = set()

for row in range(1, R + 1):
    read_row = input()
    if 'X' in read_row:
        rows_where_X.add(row)
        if read_row.count('X') > 1:
            i = 0
            while i < len(read_row):
                if read_row[i] == 'X':
                    columns_where_X.add(i + 1)
                i += 1

        else:    
            columns_where_X.add(read_row.index('X') + 1)

# print(rows_where_X)
# print(columns_where_X)

Q = int(input())
for q in range(Q):
    col, row = [int(x) for x in input().split()]
    # print(col, row)
    if row in rows_where_X or  col in columns_where_X:
        print('Y')
    else:
        print('N')


# Complexity: O(rc + q) = O(rc)
# Maximum rc = 1 000 * 1 000 = 1 000 000 (python aprox 1s = 5M operations)