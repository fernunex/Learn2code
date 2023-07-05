# Problem name: COCI '13 Contest 2 #2 Misa
# Code: coci13c2p2
# Link: https://dmoj.ca/problem/coci13c2p2

def count_hand_shakes(array_seats: list[list[bool]], R: int,S: int) -> int:
    hand_shakes = 0
    
    for i in range(1, R + 1):
        for j in range(1, S + 1):
            current_seat = array_seats[i][j]

            if current_seat:
                for k in range(i - 1, i + 2):
                    if k != 0 and k != R + 1:
                        for l in range(j - 1, j + 2):
                            if l != 0 and l != S + 1:
                                    if current_seat and array_seats[k][l]:
                                        hand_shakes += 1
                hand_shakes -= 1
                array_seats[i][j] = False
    return hand_shakes
            

# Read input
line = input().split()
R = int(line[0])
S = int(line[1])
array_seats = []
raw_seats = ''

for i in range(R + 2):
    if i == 0 or i == (R + 1):
        row = '.' * (S)
    else:
        row = input()
        raw_seats += row
    row_bools = []
    for seat in row:
        if seat == '.':
            row_bools.append(False)
        else:
            row_bools.append(True)

    row_bools.insert(0, False)
    row_bools.append(False)
    array_seats.append(row_bools)


# Check if there is seat
if '.' in raw_seats:
    # Search the seat that gives the most hand shakes
    maximum_hand_shakes = 0
    for i in range(1, R + 1):
        for j in range(1, S + 1):
            if array_seats[i][j] == False:
                array_cp = [x[:] for x in array_seats]
                array_cp[i][j] = True
                hand_shakes = count_hand_shakes(array_cp, R, S)

                if hand_shakes > maximum_hand_shakes:
                    maximum_hand_shakes = hand_shakes
    print(maximum_hand_shakes)
            
else:
    print((S-1)*(R) + (3*S - 2)*(R - 1))