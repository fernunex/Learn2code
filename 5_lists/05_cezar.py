# Problem name: COCI '17 Contest 1 #1 Cezar
# Code: coci17c1p1
# Link: https://dmoj.ca/problem/coci17c1p1

deck = []

for i in range(4):
    
    for j in range(2, 12):
        if j == 10:
            deck = deck + [j] * 4
        else:
            deck = deck + [j]

n_cards = int(input())

drew_cards = []

for i in range(n_cards):
    card_value = int(input())

    drew_cards.append(card_value)
    deck.remove(card_value)

difference = 21 - sum(drew_cards)

cards_bigger = 0

for card in deck:
    if card > difference:
        cards_bigger += 1
    
cards_lower = len(deck) - cards_bigger

if cards_bigger >= cards_lower:
    print('DOSTA')
else:
    print('VUCI')