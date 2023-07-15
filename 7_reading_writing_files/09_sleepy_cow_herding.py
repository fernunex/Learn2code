# Problem name: USACO 2019 February Contest, Bronze Problem 1. Sleepy Cow Herding
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=915

# Main
input_file = open('herding.in', 'r')
output_file = open('herding.out', 'w')

# Read input
line = input_file.readline().split()
for i in range(3):
    line[i] = int(line[i])

line.sort()

first = line[0]
second = line[1]
third = line[2]

# Checking minimum and maximum
min_moves = min(abs(first - second) - 1, abs(second - third) - 1)
max_moves = max(abs(first - second) - 1, abs(second - third) - 1)

if min_moves == 0:
    min_moves = max_moves

if min_moves >= 2:
    min_moves = 2
    


# Write output
output_file.write(str(min_moves) + '\n')
output_file.write(str(max_moves))

input_file.close()
output_file.close()