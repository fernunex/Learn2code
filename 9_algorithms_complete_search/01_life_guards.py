# Problem name:
# USACO 2018 January Contest, Bronze
# Problem 2. Lifeguards

# Link: http://usaco.org/index.php?page=viewproblem2&cpid=784

def num_covered(intervals, fired):
    """
    intervals is a list of lifeguard time intervals covered;
    each interval is a [start, end] list.
    fired is the index of the lifegurad fired.

    Return the number of time units covered by all lifeguards
    except the one fired.
    """
    time_covered = set()
    for i in range(len(intervals)):
        if i != fired:
            for j in range(intervals[i][0], intervals[i][1]):
                time_covered.add(j)
    return len(time_covered)

# Main

# Reading files
input_file = open('lifeguards.in', 'r')
output_file = open('lifeguards.out', 'w')

# Reading data
n = int(input_file.readline())

intervals = []
for _ in range(n):
    lst = input_file.readline().split()
    lst[0], lst[1] = int(lst[0]), int(lst[1])
    intervals.append(lst)

# Complete Search Algorithm
max_covered = 0
for i in range(len(intervals)):
    covered = num_covered(intervals, i)
    max_covered = covered if (covered > max_covered) else max_covered

# Writing output
output_file.write(str(max_covered))

# Closing files
input_file.close()
output_file.close()