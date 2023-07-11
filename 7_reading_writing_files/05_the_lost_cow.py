# Problem name: USACO 2017 US Open Contest, Bronze Problem 1. The Lost Cow
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=735

# Main
input_file = open('lostcow.in', 'r')
output_file = open('lostcow.out', 'w')

# Read input
line = input_file.readline().split()
x = int(line[0])
y = int(line[1])

# Calculate distance
distance = 0
if y != x:
    found = False
    step = 1

    while found == False:
        x_last = x + step
        if x < y and y <= x_last: # Found at right side
            found = True
            distance += y - x
        elif x > y and y >= x_last: # Found at left
            found = True
            distance += x - y
        else:
            distance += abs(step * 2)
            step = step * -2

# Write output
output_file.write(str(distance))

input_file.close()
output_file.close()