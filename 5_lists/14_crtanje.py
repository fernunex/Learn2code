# Problem name: COCI '20 Contest 2 #1 Crtanje
# Code: coci20c2p1
# Link: https://dmoj.ca/problem/coci20c2p1

days = int(input())
line = input()

matrix = []

for _ in range(200):
    matrix.append('.' * len(line))

x = 0

for i in range(days):
    if line[i] == '+':
        index = x + 100
        x += 1
        matrix[index] = matrix[index][:i] + '/' + matrix[index][i + 1:]


    elif line[i] == '-':
        x -= 1
        index = x + 100
        matrix[index] = matrix[index][:i] + '\\' + matrix[index][i + 1:]

    else:
        index = x + 100
        matrix[index] = matrix[index][:i] + '_' + matrix[index][i + 1:]


for row in matrix[::-1]:
    if '/' in row or '\\' in row or '_' in row:
        print(row)