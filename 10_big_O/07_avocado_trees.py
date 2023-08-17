# Problem name: Avocado Trees!
# Code: avocadotrees
# Link: https://dmoj.ca/problem/avocadotrees


# # Solved
# # Fast input/output
# import sys
# input = sys.stdin.readline

# N, Q, H = map(int, input().split())

# accumulated = {0: (0,0)}
# total = 0

# for tree in range(1, N + 1):
#     height, production = map(int, input().split())
#     if height <= H:
#         total += production
#         accumulated[tree] = (total, production)
#     else:
#         accumulated[tree] = (total, 0)

# max_avocados = 0
# for query in range(Q):
#     initial, final = map(int, input().split())
#     robbed = accumulated[final][0] - accumulated[initial][0] + accumulated[initial][1]
#     max_avocados = robbed if robbed > max_avocados else max_avocados

# print(max_avocados)

# # Complexity O(n + q)

###### This is faster
# Fast input/output
import sys
input = sys.stdin.readline

N, Q, H = map(int, input().split())

accumulated = [0]
total = 0

for tree in range(1, N + 1):
    height, production = map(int, input().split())
    if height <= H:
        total += production
        accumulated.append(total)
    else:
        accumulated.append(total)


max_avocados = 0
for query in range(Q):
    initial, final = map(int, input().split())
    robbed = accumulated[final] - accumulated[initial - 1]
    max_avocados = robbed if robbed > max_avocados else max_avocados

print(max_avocados)