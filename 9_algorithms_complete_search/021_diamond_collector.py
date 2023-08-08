# Problem name:
# USACO 2016 US Open Contest, Bronze
# Problem 1. Diamond Collector

# Link: http://usaco.org/index.php?page=viewproblem2&cpid=639

def similar_diamonds(diamonds, index, difference):
    """
    diamonds is a list of the diamonds' sizes.
    index is the low value for the range.
    difference is an integer that determinate the high value for
    the range.

    Return how many diamonds are in the range.
    """
    n_diamonds = 0
    low = diamonds[index]
    high = diamonds[index] + difference

    for i in range(len(diamonds)):
            if low <= diamonds[i] and diamonds[i] <= high:
                n_diamonds += 1
    return n_diamonds



# Main
input_file = open('diamond.in', 'r')
output_file = open('diamond.out', 'w')

N, K = [int(x) for x in input_file.readline().strip().split()]

diamonds = []
for _ in range(N):
    diamonds.append(int(input_file.readline().strip()))

max_case_diamonds = 0
for i in range(N):
    caseable_diamond = similar_diamonds(diamonds, i, K)
    if caseable_diamond > max_case_diamonds:
        max_case_diamonds = caseable_diamond

output_file.write(str(max_case_diamonds))

input_file.close()
output_file.close()