# Problem name: COCI '13 Contest 3 #1 Riječi
# Code: coci13c3p1
# Link: https://dmoj.ca/problem/coci13c3p1

# A --> B
# B --> BA

k = int(input ())
a = 1
b = 0

for i in range(k):
    a_counter = a
    b_counter = b
    if not(a == 0):
        b_counter += 1*a
        a_counter -= 1*a
    if not(b == 0):
        a_counter += 1*b
    
    a = a_counter
    b = b_counter
    
print(a,b)