# Problem name: DMOPC '20 Contest 2 P2 - Lousy Christmas Presents
# Code: dmopc20c2p2
# Link: https://dmoj.ca/problem/dmopc20c2p2

n, m = [int(x) for x in input().split()]

leftmost_index = {}
rightmost_index = {}

scarf = input().split()

for i in range(n):
    color = scarf[i]
    if color in leftmost_index:
        rightmost_index[color] = i
    else:
        leftmost_index[color] = i
        rightmost_index[color] = i

longest = 0
for _ in range(m):
    left, right = input().split()
    if left in leftmost_index and right in rightmost_index:
        length = rightmost_index[right] - leftmost_index[left] + 1
        if length > longest:
            longest = length

print(longest)