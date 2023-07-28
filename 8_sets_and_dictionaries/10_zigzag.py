# Problem name: COCI '17 Contest 2 #2 ZigZag
# Code: coci17c2p2
# Link: https://dmoj.ca/problem/coci17c2p2

## Too Slow

# def choose_word(word_dict: dict[str:dict], letter:str):
#     apparences = list(word_dict[letter].values())
#     min_apparences = min(apparences)
    
#     # Check if it is ambiguos
#     if apparences.count(min_apparences) > 1:
#         candidates = [word 
#                     for word, counter in word_dict[letter].items()
#                     if counter == min_apparences]
#         candidates.sort()
#         word_chosen = candidates[0]
#         word_dict[letter][word_chosen] += 1
        
#         return word_chosen
    
#     else:
#         for word, value in word_dict[letter].items():
#             if value == min_apparences:
#                 word_dict[letter][word] += 1
#                 return word


# # Main
# import sys

# input = sys.stdin.readline

# lst = input().split()
# K_words, N_letters = int(lst[0]), int(lst[1])

# # Reading data

# # Words
# word_dict = {}
# for _ in range(K_words):
#     word = input().strip()
#     letter = word[0]
    
#     if letter not in word_dict:
#         word_dict[letter] = {word:0}
#     else:
#         word_dict[letter] = word_dict[letter] | {word:0}

# # Letters
# output_words = []
# for _ in range(N_letters):
#     letter = input().strip()
#     word_selected = choose_word(word_dict, letter)
#     output_words.append(word_selected)

# print('\n'.join(output_words))

## Second version

def choose_word(word_dict: dict[str:dict], letter:str):
    chose_word = word_dict[letter].pop(0)
    word_dict[letter].append(chose_word)
    return chose_word
    

# Main
import sys

input = sys.stdin.readline

lst = input().split()
K_words, N_letters = int(lst[0]), int(lst[1])

# Reading data

# Words
word_dict = {}
for _ in range(K_words):
    word = input().strip()
    letter = word[0]
    
    if letter not in word_dict:
        word_dict[letter] = [word]
    else:
        word_dict[letter].append(word)

for letter in word_dict:
    word_dict[letter].sort()

# Letters
output_words = []
for _ in range(N_letters):
    letter = input().strip()
    word_selected = choose_word(word_dict, letter)
    output_words.append(word_selected)

print('\n'.join(output_words))