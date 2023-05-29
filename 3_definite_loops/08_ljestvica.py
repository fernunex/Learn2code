# Problem name: COCI '12 Contest 5 #1 Ljestvica
# Code: coci12c5p1
# Link: https://dmoj.ca/problem/coci12c5p1

# total tones :A, B, C, D, E, F, G
sequence = input()
a_minor = 'ADE'
c_major = 'CFG'


a_counter = 0
c_counter = 0

tones = sequence.split('|')

for tone in tones:
    if tone[0] in a_minor:
        a_counter += 1
    elif tone[0] in c_major:
        c_counter += 1

if a_counter > c_counter:
    print('A-mol')
elif c_counter > a_counter:
    print('C-dur')
else:
    if tones[-1][-1] in 'A':
        print('A-mol')
    else:
        print('C-dur')




