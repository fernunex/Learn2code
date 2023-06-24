# Problem name: COCI '19 Contest 5 #1 Emacs
# Code: coci19c5p1
# Link: https://dmoj.ca/problem/coci19c5p1

n_m = input().split()
high = int(n_m[0])
wide = int(n_m[1])

picture = []

for _ in range(high):
    picture.append(input())

rectangles = 0

for i in range(high):

    for j in range(wide):

        if i == 0:
            if picture[0][j] == '*':
                if j < (wide - 1) and picture[0][j + 1] == '.':
                    rectangles += 1
                elif j == (wide - 1) and picture[0][j] == '*':
                    rectangles += 1

        else:
            if picture[i][j] == '*' and picture[i - 1][j] == '.':
                if j < (wide - 1) and picture[i][j + 1] == '.' :
                    rectangles += 1 
                elif j == (wide - 1) and picture[i][j] == '*':
                    rectangles += 1


print(rectangles)