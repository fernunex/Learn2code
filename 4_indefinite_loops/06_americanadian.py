# Problem name: CCC '02 J2 - AmeriCanadian
# Code: ccc02j2
# Link: https://dmoj.ca/problem/ccc02j2

vowels = 'aeiouy'
words = ''

while True:
    word = input()
    if word == 'quit!':
        break
    else:
        if len(word) > 4:

            if word[-2:] == 'or' and (word[-3] not in vowels): #its american then change to canadian
                words = words + word[:-2] + 'our' + '\n'
            elif word[-3] == 'our' and (word[-4] not in vowels): #its canadian then change to american
                words = words + word[:-3] + 'or' + '\n'
            else:
                words = words + word + '\n'
        else:
                words = words + word + '\n'
    
print(words[:-1])