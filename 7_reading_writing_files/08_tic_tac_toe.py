# Problem name: USACO 2018 US Open Contest, Bronze Problem 1. Team Tic Tac Toe
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=831

def check_won_before(winners, new_winner):
    """
    winners is a list of cows that had already won
    new_winner is a list of 1 or more cows that just won

    return True if that cow or cows have already won, False otherwise 
    """
    if len(new_winner) == 1:
        return new_winner in winners
    else:
        return ((new_winner in winners) or 
                ([new_winner[1], new_winner[0]] in winners))


def calculate_winners(board, no_team):
    """
    board is a grid that contais the gameboard of the match
    no_team refers to how many cows are team to win the match

    return how many teams of cows (can be only one cow) win in 
    the current match.
    """
    winners = []
    limit = no_team

    # Columns
    for i in range(3):
        first = board[0][i]
        winner = [first]
        j = 1
        while j < 3:
            # print(f'{first} vs {board[j][i]}')
            if board[j][i] not in winner:
                winner.append(board[j][i])
            j += 1
        if len(winner) == limit:
            if not check_won_before(winners, winner):
                winners.append(winner)
    
    # Rows
    for i in range(3):
        first = board[i][0]
        winner = [first]
        j = 1
        while j < 3:
            # print(f"{i},{j}")
            # print(f'{board[i][j]}')
            if board[i][j] not in winner:
                winner.append(board[i][j])
            j += 1
        if len(winner) == limit:
            if not check_won_before(winners, winner):
                winners.append(winner)


    # Diagonal Left to Right
    first = board[0][0]
    winner = [first]
    for i in range(1, 3):
        if board[i][i] not in winner:
            winner.append(board[i][i])
        
    if len(winner) == limit:
        if not check_won_before(winners, winner):
            winners.append(winner)

    # Diagonal Right to left
    first = board[0][2]
    winner = [first]
    for i in range(1, 3):
        # print(f'{first} vs {board[i][2 - i]}')
        if board[i][2 - i] not in winner:
            winner.append(board[i][2 - i])
        
    if len(winner) == limit:
        if not check_won_before(winners, winner):
            winners.append(winner)

    return len(winners)


# Main
input_file = open('tttt.in', 'r')
output_file = open('tttt.out', 'w')

# Read Board
board = []
for line in input_file:
    board.append(line.rstrip())


# Calculate winners Team of 1 cow
number_winners_solo = calculate_winners(board, 1)

# Calculate winners Team of 2 cows
number_winners_team = calculate_winners(board, 2)

# Write Output
output_file.write(str(number_winners_solo) + '\n')
output_file.write(str(number_winners_team))


input_file.close()
output_file.close()