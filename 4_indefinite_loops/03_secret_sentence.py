# Problem name: COCI '08 Contest 3 #2 Kemija
# Code: coci08c3p2
# Link: https://dmoj.ca/problem/coci08c3p2

secret_string = input()
real = ''
i = 0

while i < len(secret_string):
    real = real + secret_string[i]
    if secret_string[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1

print(real)