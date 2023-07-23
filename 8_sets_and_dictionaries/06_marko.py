# Problem name: COCI '15 Contest 2 #1 Marko
# Code: coci15c2p1
# Link: https://dmoj.ca/problem/coci15c2p1

KEYBOARD = {
    'abc': 2,
    'def': 3,
    'ghi': 4,
    'jkl': 5,
    'mno': 6,
    'pqrs': 7,
    'tuv': 8,
    'wxyz': 9
}

def word_to_presses(word, KEYBOARD):
    """
    word is any string in lowercase.
    KEYBOARD is a dictionary where key are the letters and the value
    is the keyboard key asigned to those letters.

    Retruns a list of keyboard key for each letter of the word (maps
    from letters to numbers).
    """
    code_number = []
    for lettter in word:
        for key in KEYBOARD:
            if lettter in key:
                code_number.append(KEYBOARD[key])
                break
    return code_number


# Main
N = int(input())

# Rcording Input
dictionary = []
for _ in range(N):
    dictionary.append(input())

S = input()
S_lst = []
for i in range(len(S)):
    S_lst.append(int(S[i]))

# Counting words
count_words = 0
for word in dictionary:
    number_code = word_to_presses(word, KEYBOARD)
    if S_lst == number_code:
        count_words += 1

# Output
print(count_words)