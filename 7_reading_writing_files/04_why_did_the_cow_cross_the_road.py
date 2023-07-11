# Problem name: USACO 2017 February Contest, Bronze Problem 1. Why Did the Cow Cross the Road
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=711

# Main
input_file = open('crossroad.in', 'r')
output_file = open('crossroad.out', 'w')

# Record all crosses
n_records = int(input_file.readline())
records = [[0],[],[],[],[],[],[],[],[],[],[]] # 10 cows start at index 1

for record in input_file:
    line = record.split()
    records[int(line[0])].append(int(line[1]))

# Calculate crosses
crosses = 0
for cow in records:
    for i in range(len(cow) - 1):
        if (cow[i] + cow[i + 1]) == 1:
            crosses += 1

# Write output
output_file.write(str(crosses))

input_file.close()
output_file.close()