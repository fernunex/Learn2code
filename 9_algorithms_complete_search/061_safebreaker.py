# Problem name: CCO '96 P2 - SafeBreaker
# Code: cco96p2
# Link: https://dmoj.ca/problem/cco96p2


# I read the solution of Daniel Zingaro
# This problem was hard for me

def consistent_guess(code, guess):
    """
    code is any number to test
    guess is list of [code, corrects, misplaced]

    Return True if the code generates the same
    combination of corrects and misplaced for the code
    guessed
    """

    code_guess = list(guess[0])
    code = list(code)
    
    corrects = 0
    misplaced = 0

    # Check corrects
    for i in range(len(code)):
        if code_guess[i] == code[i]:
            corrects += 1
            code_guess[i] = ''
            code[i] = ''
    
    # Check misplaced
    for i in range(len(code)):
        if code[i] != '' and code[i] in code_guess:
            code_guess[code_guess.index(code[i])] = ''
            misplaced += 1
        
    return corrects == guess[1] and misplaced == guess[2]


def all_guesses_consistent(code, guesses):
    """
    code is a number
    guesses is a list of guesses

    Return True if the code satisfy all the guesses, False
    otherwise
    """

    for guess in guesses:
        if not consistent_guess(code, guess):
            return False
    return True

def correct_string(guesses):
    """
    guesses is a list of guesses and the feedback

    Return: 
        'indeterminate' if there is more than one secret
        code that satisfy all guesses.

        'imposible' if there is any number that satisfy all
        the guesses
        
        secret_number if there is only one number that satisfy
        all the guesses 
    """
    codes_consistent = 0
    for n1 in NUMS:
        for n2 in NUMS:
            for n3 in NUMS:
                for n4 in NUMS:
                    posible_code = n1 + n2 + n3 + n4
                    if all_guesses_consistent(posible_code, guesses):
                        codes_consistent += 1
                        secret_code = posible_code
                        if codes_consistent > 1:
                            return 'indeterminate'

    if codes_consistent == 0:
        return 'impossible'
    else:
        return secret_code



# Main
NUMS = '0123456789'

n_dataset = int(input())

for _ in range(n_dataset):
    G = int(input())

    guesses = []
    for _ in range(G):
        lst = input().split()
        guesses.append([lst[0], int(lst[1][0]), int(lst[1][-1])])

    print(correct_string(guesses))