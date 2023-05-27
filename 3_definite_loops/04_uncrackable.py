# Problem name: WC '17 Contest 3 J3 - Uncrackable
# Code: wc17c3j3
# Link: https://dmoj.ca/problem/wc17c3j3

# 8-12 Char
# >= 3 lowercase letters
# >= 2 uppercase letters
# >= 1 digit

# Output : Valid or Invalid

password = input()
lowercase = 0
uppercase = 0
digits = 0

for char in password:
    if char.islower():
        lowercase += 1
    if char.isupper():
        uppercase += 1
    if char.isdigit():
        digits += 1

if (lowercase >= 3 and 
    uppercase >= 2 and 
    digits >= 1 and
    len(password) >= 8 and len(password) <= 12):
    print('Valid')
else:
    print('Invalid')