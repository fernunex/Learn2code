# Problem name: DMOPC '16 Contest 1 P0 - C.C. and Cheese-kun
# Code: dmopc16c1p0
# Link: https://dmoj.ca/problem/dmopc16c1p0

# inputs
width = int(input())
cheese = int(input())
satisfaction = ''

if width == 3 and cheese >= 95:
    satisfaction = 'absolutely'
elif width == 1 and cheese <= 50:
    satisfaction = 'fairly'
else:
    satisfaction = 'very'


print(f"C.C. is {satisfaction} satisfied with her pizza.")