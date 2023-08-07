# Problem name:
# USACO 2016 December Contest, Silver
# Problem 1. Counting Haybales

# Link: http://usaco.org/index.php?page=viewproblem2&cpid=666

from bisect import bisect_right, bisect_left

input_file = open('haybales.in', 'r')
output_file = open('haybales.out', 'w')

N, Q = [int(x) for x in input_file.readline().split()]
haybales_positions = list(int(x) for x in input_file.readline().split())
haybales_positions.sort()

for _ in range(Q):
    total = 0
    low_num, max_num = [int(x) for x in input_file.readline().split()]

    in_0 = bisect_left(haybales_positions, low_num)
    in_1 = bisect_right(haybales_positions, max_num)
    
    output_file.write(str(in_1 - in_0) + '\n')

input_file.close()
output_file.close()