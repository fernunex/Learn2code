# Problem name: CCC '18 J2 - Occupy parking
# Code: ccc18j2
# Link: https://dmoj.ca/problem/ccc18j2

n = int(input())
yesterday = input()
today = input()
occupied_spaces = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied_spaces += 1

print(occupied_spaces)