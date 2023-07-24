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
# I was missing something hahha

complete_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
plaintext = input()
ciphertext = input()
ciphertext_to_decode = input()

cipher_decoded = {}

for i in range(len(plaintext)):
    cipher_decoded[ciphertext[i]] = plaintext[i]

if len(cipher_decoded) == 26: # Just is missing one word, we can predict
    cipher_decoded[(complete_chars - (cipher_decoded.keys())).pop()] = (complete_chars - set(cipher_decoded.values())).pop()

plain_decoded = ''
for i in range(len(ciphertext_to_decode)):
    if ciphertext_to_decode[i] in cipher_decoded:
        plain_decoded += cipher_decoded[ciphertext_to_decode[i]]
    else:
        plain_decoded += '.'

print(plain_decoded)

# Third verions form other developer hellobye65536
# pt = input()
# cpt = input()
# ct = input()

# cs = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

# cd = {}
# for p, c in zip(pt, cpt):
#     cd[c] = p

# if len(cd) == 26:

# print(''.join(map(lambda k: cd.get(k, '.'), ct)))

# TMFPNOQLRPHYK IPUKVPGOEADPKBFYPTMFPJCZXPWK
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DO
# TMFPWKSPCIWPTMFPUKV