# Problem name: ECOO '13 R1 P1 - Take a Number
# Code: ecoo13r1p1
# Link: https://dmoj.ca/problem/ecoo13r1p1

next_number = int(input())
takes = 0
serves = 0
line = ''

while line != 'EOF':
    line = input()
    if line == 'TAKE':
        takes = takes + 1
        next_number = next_number + 1

    elif line == 'SERVE':
        takes = takes - 1
        serves = serves + 1

    elif line == 'CLOSE':
        serves = serves + takes
        print(f'{serves} {takes} {next_number}')
        serves = 0
        takes = 0

    if next_number == 1000:
        next_number = 1