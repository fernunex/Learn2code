# Problem name:
# USACO 2019 January Contest, Bronze
# Problem 1. Shell Game
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=891

def calculate_score(pebbel_location, swaps, choices):

    score = 0
    i = 0
    for swap in swaps:
        a = swap[0]
        b = swap[1]
        pebbel_location[a], pebbel_location[b] = pebbel_location[b], pebbel_location[a]
        if pebbel_location[choices[i]]:
            score += 1
        i += 1
    return score

# Main
input_file = open('shell.in', 'r')
output_file = open('shell.out', 'w')

N = int(input_file.readline())

swaps = []
choices = []

for _ in range(N):
    lst = input_file.readline().split()
    swaps.append([int(lst[0]) - 1, int(lst[1]) - 1])
    choices.append(int(lst[2]) - 1)

max_score = 0
for i in range(3):
    pebbel_location = [False, False, False]
    pebbel_location[i] = True

    score = calculate_score(pebbel_location, swaps, choices)
    if score > max_score:
        max_score = score

output_file.write(str(max_score))

input_file.close()
output_file.close()