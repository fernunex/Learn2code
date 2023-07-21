# Problem name: COCI '06 Regional #1 Bard
# Code: crci06p1
# Link: https://dmoj.ca/problem/crci06p1

# Read Input
N_villagers = int(input())
E_evenings = int(input())

nights = []

for _ in range(E_evenings):
    villagers = input().split()
    for i in range(int(villagers[0]) + 1):
        villagers[i] = int(villagers[i])

    if 1 in villagers[1:]:
        nights.append(set(villagers[1:]))
    else:
        for villager in villagers[1:]:
            for night in nights:
                if villager in night:
                    night.update(set(villagers[1:]))

for i in range(1, N_villagers + 1):
    all_songs = True
    for night in nights:
        if i not in night:
            all_songs = False
            break
    if all_songs:
        print(i)