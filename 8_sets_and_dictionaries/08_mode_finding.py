# Problem name: DMOPC '19 Contest 3 P1 - Mode Finding
# Code: dmopc19c3p1
# Link: https://dmoj.ca/problem/dmopc19c3p1

N = int(input())
numbers = input().split()

numbers_counted = {}
for number in numbers:
    if number not in numbers_counted:
        numbers_counted[number] = 1
    else:
        numbers_counted[number] += 1

max_counted = max(set(numbers_counted.values()))

modes = [int(num) for num, count in numbers_counted.items() if count == max_counted]
modes.sort()

for i in range(len(modes)):
    modes[i] = str(modes[i])

print(' '.join(modes))



# Check the FASTEST SOLUTION by Subway_Man
# from collections import Counter
# f = input()
# g = Counter(input().split()).most_common()
# mode = g[0][1]
# yes = []
# for e in g:
    # if e[1] != mode:
        # break
    # yes.append(e[0])

# print(*sorted(yes, key=int))