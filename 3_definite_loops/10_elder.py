# Problem name: COCI '18 Contest 4 #1 Elder
# Code: coci18c4p1
# Link: https://dmoj.ca/problem/coci18c4p1

owner_wand = input()
number_duels = int(input())
owners = owner_wand

for _ in range(number_duels):
    duel = input()

    if duel[-1] == owner_wand:
        owner_wand = duel[0]
        if owner_wand not in owners:
            owners += owner_wand
    
print(owner_wand)
print(len(owners))
