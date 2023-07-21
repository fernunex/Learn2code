# Problem name: DMOPC '19 Contest 5 P1 - Conspicuous Cryptic Checklist
# Code: dmopc19c5p1
# Link: https://dmoj.ca/problem/dmopc19c5p1

# Read Inputs
line = [int(x) for x in input().split()]
N_items = line[0]
M_assignments = line[1]
requirements_completed = 0

items = set()
for _ in range(N_items):
    items.add(input())

# Check that assignments' requirements meets items
for _ in range(M_assignments):
    T_items = int(input())
    required = set()

    for _ in range(T_items):
        required.add(input())

    if required.issubset(items):
        requirements_completed += 1

print(requirements_completed)