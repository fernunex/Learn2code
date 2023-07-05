# Problem name: COCI '13 Contest 2 #2 Misa
# Code: coci13c2p2
# Link: https://dmoj.ca/problem/coci13c2p2

def num_neighbours(grid, row, col):
    last_row = len(grid) - 1 
    last_col = len(grid[0]) - 1
    total = 0

    # Check all directions

    # Right
    if col < last_col and grid[row][col + 1] == 'o':
        total += 1
    # Left
    if col > 0 and grid[row][col - 1] == 'o':
        total += 1
    # Down
    if row < last_row and grid[row + 1][col] == 'o':
        total += 1
    # Up
    if row > 0 and grid[row - 1][col] == 'o':
        total += 1
    # Right down
    if col < last_col and row < last_row and grid[row + 1][col + 1] == 'o':
        total += 1
    # Right up
    if row > 0 and col < last_col and grid[row - 1][col + 1] == 'o':
        total += 1
    # Left down
    if col > 0 and  row < last_row and grid[row + 1][col - 1] == 'o':
        total += 1
    # Left up
    if row > 0 and col > 0 and grid[row - 1][col - 1] == 'o':
        total += 1
    
    return total



def mirko_location(grid):
    mirko_row, mirko_col = -1, -1
    most = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '.':
                neighbours = num_neighbours(grid, row, col)
                if neighbours > most:
                    most = neighbours
                    mirko_row = row
                    mirko_col = col
    return [mirko_row, mirko_col]




# Read input
line = input().split()
R = int(line[0])
S = int(line[1])
array_seats = []

for _ in range(R):
    array_seats.append(list(input()))

# Mirko location
lst = mirko_location(array_seats)
mirko_row = lst[0]
mirko_col = lst[1]
if mirko_row >= 0 and mirko_col >= 0:
    array_seats[mirko_row][mirko_col] = 'o' # Sits in that position

# Count handshakes
handshakes = 0
for row in range(R):
    for col in range(S):
        if array_seats[row][col] == 'o':
            handshakes += num_neighbours(array_seats, row, col)

handshakes = handshakes // 2 # For every person that give twice handsakes; 
                            # A -> B and B -> A count as one handshake
print(handshakes)