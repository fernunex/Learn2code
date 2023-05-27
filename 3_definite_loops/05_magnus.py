# Problem name: COCI '18 Contest 3 #1 Magnus
# Code: coci18c3p1
# Link: https://dmoj.ca/problem/coci18c3p1

#HONI

word = input()
h_s = 0
o_s = 0
n_s = 0
i_s = 0

for char in word:
    if char == 'H' and h_s == i_s:
        h_s += 1
    elif char == 'O' and o_s + 1 == h_s:
        o_s += 1
    elif char == 'N' and n_s + 1 == o_s:
        n_s += 1
    elif char == 'I' and i_s + 1 == n_s:
        i_s += 1

print(i_s)

