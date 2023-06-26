# Problem name: CCC '99 S1 - Card Game
# Code: ccc99s1
# Link: https://dmoj.ca/problem/ccc99s1

NUM_CARDS = 52

def no_high(lst: list):
    """This fuction returns True if there is no high cards (jack, queen,
    king or ace) in the list.

    Args:
        lst (list): List of cards

    Returns:
        True: if there is no high cards on the list passed
        False: if there is high cards on the list passed
    """
    if 'jack' in lst:
        return False
    if 'queen' in lst:
        return False
    if 'king' in lst:
        return False
    if 'ace' in lst:
        return False
    return True

deck = []

for _ in range(NUM_CARDS):
    deck.append(input())

score_a = 0
score_b = 0
player = 'A'

for i in range(NUM_CARDS):
    card = deck[i]
    points = 0
    remaining_cards = NUM_CARDS - i - 1

    if card == 'jack' and remaining_cards >= 1 and no_high(deck[i+1:i+2]):
        points = 1

    elif card == 'queen' and remaining_cards >= 2 and no_high(deck[i+1:i+3]):
        points = 2
    
    elif card == 'king' and remaining_cards >= 3 and no_high(deck[i+1:i+4]):
        points = 3
    
    elif card == 'ace' and remaining_cards >= 4 and no_high(deck[i+1:i+5]):
        points = 4

    if points > 0:
        print(f"Player {player} scores {points} point(s).")

    if player == 'A':
        score_a += points
        player = 'B'
    else:
        score_b += points
        player = 'A'

print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')