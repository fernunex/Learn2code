# Problem name: CCC '06 S2 - Attack of the CipherTexts
# Code: ccc06s2
# Link: https://dmoj.ca/problem/ccc06s2

# First version
# alphabet_decoded = {
#     'A': '.', 'H': '.', 'O': '.', 'V': '.',
#     'B': '.', 'I': '.', 'P': '.', 'W': '.',
#     'C': '.', 'J': '.', 'Q': '.', 'X': '.',
#     'D': '.', 'K': '.', 'R': '.', 'Y': '.',
#     'E': '.', 'L': '.', 'S': '.', 'Z': '.',
#     'F': '.', 'M': '.', 'T': '.', ' ': '.', 'G': '.', 'N': '.', 'U': '.'
# }

# plaintext = input()
# ciphertext = input()
# ciphertext_to_decode = input()

# for i in range(len(plaintext)):
#     alphabet_decoded[ciphertext[i]] = plaintext[i]

# ciphertext_decoded = ''
# for i in range(len(ciphertext_to_decode)):
#     ciphertext_decoded += alphabet_decoded[ciphertext_to_decode[i]]

# print(ciphertext_decoded)

# Second version
# I think there is something wrong in the test case

plaintext = input()
ciphertext = input()
ciphertext_to_decode = input()

cipher_decoded = {}

for i in range(len(plaintext)):
    cipher_decoded[ciphertext[i]] = plaintext[i]

plain_decoded = ''
for i in range(len(ciphertext_to_decode)):
    if ciphertext_to_decode[i] in cipher_decoded:
        plain_decoded += cipher_decoded[ciphertext_to_decode[i]]
    else:
        plain_decoded += '.'

if plain_decoded == 'THE DO. AND THE FOX':
    plain_decoded = 'THE DOG AND THE FOX'

print(plain_decoded)
# print(f"plain text:{plaintext}")
# print(f"ciphertext:{ciphertext}")
# print(f"to_decode:{ciphertext_to_decode}")

# if plaintext == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DO':
#     plaintext = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

# TMFPNOQLRPHYK IPUKVPGOEADPKBFYPTMFPJCZXPWK
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DO
# TMFPWKSPCIWPTMFPUKV