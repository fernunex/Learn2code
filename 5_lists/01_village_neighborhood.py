# Problem name: CCC '18 S1 - Voronoi Villages
# Code: ccc18s1
# Link: https://dmoj.ca/problem/ccc18s1

n = int(input())

positions = []
sizes = []

for _ in range(n):
    positions.append(int(input()))

positions.sort()

for i in range(1, n - 1):
    left = (positions[i] - positions[i - 1]) / 2
    right = (positions[i + 1] - positions[i]) / 2
    sizes.append(left + right)

print(min(sizes))
