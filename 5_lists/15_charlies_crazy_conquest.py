# Problem name: DMOPC '19 Contest 5 P2 - Charlie's Crazy Conquest
# Code: dmopc19c5p2
# Link: https://dmoj.ca/problem/dmopc19c5p2

line = input().split()
n_attacks = int(line[0])
health = int(line[1])

attacks_charlie = []
attacks_bot = []
health_charlie = health
health_bot = health

for _ in range(n_attacks):
    input_attack = input().split()
    input_attack[-1] = int(input_attack[-1])
    attacks_charlie.append(input_attack)

for _ in range(n_attacks):
    input_attack = input().split()
    input_attack[-1] = int(input_attack[-1])
    attacks_bot.append(input_attack)

i = 0

while i < len(attacks_charlie) and health_charlie > 0 and health_bot > 0:
    if attacks_charlie[i][0] == 'A' and (i == 0 or attacks_bot[i - 1][0] == 'A'):
        health_bot -= attacks_charlie[i][1]
    elif attacks_charlie[i][0] == 'D' and attacks_bot[i][0] == 'D':
        health_charlie -= attacks_charlie[i][1]

    if health_charlie > 0 and health_bot > 0:
        if attacks_bot[i][0] == 'A' and attacks_charlie[i][0] == 'A':
            health_charlie -= attacks_bot[i][1]
        elif attacks_bot[i][0] == 'D' and (i == n_attacks - 1 or attacks_charlie[i + 1][0] == 'D'):
            health_bot -= attacks_bot[i][1]

    i += 1



if 0 >= health_bot:
    print('VICTORY')
elif health_charlie <= 0 :
    print('DEFEAT')
else:
    print('TIE')