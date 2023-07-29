# Problem name:
# USACO 2014 January Contest, Bronze
# Problem 1. Ski Course Design

# Link: http://usaco.org/index.php?page=viewproblem2&cpid=376

def cost_for_range(hills: list, low, high):
    """
    hills is a list of the hills' heights.
    low is a integer giving the low end of the range.
    high is a integer giving the high end of the range.

    Return the cost of changing all heights of hills to be 
    between low an high.
    """
    cost = 0
    for hill in hills:
        if hill < low:
            cost += (hill - low) ** 2
        elif hill > high:
            cost += (hill - high) ** 2
    return cost

# Main 
MAX_DIFFERENCE = 17
MAX_HEIGHT = 100 

input_file = open('skidesign.in', 'r')
output_file = open('skidesign.out', 'w')

N = int(input_file.readline())

hills = []
for _ in range(N):
    hills.append(int(input_file.readline()))

min_cost = cost_for_range(hills, 0, MAX_DIFFERENCE)

for i in range(1, MAX_HEIGHT + 1):
    cost = cost_for_range(hills, i, i + MAX_DIFFERENCE)
    if min_cost > cost:
        min_cost = cost

output_file.write(str(min_cost))

input_file.close()
output_file.close()