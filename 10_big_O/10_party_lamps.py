# Problem name: IOI '98 P3 - Party Lamps
# Code: ioi98p3
# Link: https://dmoj.ca/problem/ioi98p3

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
C = int(input())

# Saving Lights On
lights_on = list(map(int,input().split()))
lights_on.pop()

lights_off = list(map(int,input().split()))
lights_off.pop()

sequences = set()

for button_1 in [0,1]:
    for button_2 in [0,1]:
        for button_3 in [0,1]:
            for button_4 in [0,1]:
                if (button_1 + button_2 + button_3 + button_4) > C:
                    continue
                if (button_1 + button_2 + button_3 + button_4) % 2 != C % 2:
                    continue

                # all start on 
                sequence = [1] * N
                
                # 1 All change state
                if button_1 == 1:
                    sequence = [0] * N
                
                # 2 Change odd
                if button_2 == 1:
                    for i in range(0, N, 2):
                        sequence[i] = 1 - sequence[i] 
                # 3 Change even
                if button_3 == 1:
                    for i in range(1, N, 2):
                        sequence[i] = 1 - sequence[i]
                # 4 Change every 3 lamps
                if button_4 == 1:
                    for i in range(0, N, 3):
                        sequence[i] = 1 - sequence[i]

                # Check if this sequence meets the information on 
                # the final state of some of the lamps.
                meets_requirements = True
                for i in lights_on:
                    if sequence[i - 1] == 0:
                        meets_requirements = False
                        break
                
                if meets_requirements:
                    for i in lights_off:
                        if sequence[i - 1] == 1:
                            meets_requirements = False
                            break

                if meets_requirements:
                    sequences.add(tuple(sequence))

if sequences:
    for seq in sequences:
        seq = list(map(str, seq))
        print(''.join(seq))
        print('\n')
else:
    print('IMPOSSIBLE')