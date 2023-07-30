#!/usr/bin/python3
# Problem name:
# USACO 2013 December Contest, Bronze
# Problem 2. Cow Baseball

# Link: http://usaco.org/index.php?page=viewproblem2&cpid=359

# Main
from bisect import bisect_left, bisect_right

input_file = open('baseball.in', 'r')
output_file = open('baseball.out', 'w')

N = int(input_file.readline())
print(N)

positions = []
for _ in range(N):
    positions.append(int(input_file.readline()))

positions.sort()
total = 0
for i in range(N):
    for j in range(i + 1, N):
        diff = positions[j] - positions[i]
        low = positions[j] + diff
        high = positions[j] + diff * 2
        left = bisect_left(positions[j:], low)
        right = bisect_right(positions[j:], high)
        total += right - left

output_file.write(str(total))

input_file.close()
output_file.close()