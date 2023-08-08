# Problem name: ECOO '16 R1 P2 - Spindie
# Code: ecoo16r1p2
# Link: https://dmoj.ca/problem/ecoo16r1p2

# Main
# Reimplement and experimentation idea: https://dmoj.ca/user/DREU007
import sys
input = sys.stdin.readline

for _ in range(10):
    N = input()
    numbers = set(map(int, input().split()))
    targets = list(map(int, input().split()))


    posibilities = set()
    for num1 in numbers:
        for num2 in numbers:
            posibilities.update({num1 + num2, num1 * num2})

    for target in targets:
        found = 'F'
        for num in numbers:
            if (target// num in posibilities and target % num == 0) or (target - num) in posibilities:
                found = 'T'

        print(found, sep='', end='')
        
    print()