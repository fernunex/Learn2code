# Problem name: ECOO '16 R1 P2 - Spindie
# Code: ecoo16r1p2
# Link: https://dmoj.ca/problem/ecoo16r1p2

def generate_combinations(num1, num2, num3):
    """
    num1, num2 and num3 are the posible oucomes form the spinner.

    Return all the combination of multiplication and sum posibles between
    those numbers.
    """
    return {
            ((num1 + num2) + num3),
            ((num1 + num2) * num3),
            ((num1 * num2) + num3),
            ((num1 * num2) * num3)
    }


# Main
import sys
input = sys.stdin.readline

for _ in range(10):
    N = input()
    numbers = set(map(lambda x: int(x), input().split()))
    targets = list(map(lambda x: int(x), input().split()))

    upper_limit = max(targets)
    lower_limit = min(targets)

    posibilities = set()
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                combination = generate_combinations(num1, num2, num3)
                posibilities.update(set(filter(
                    lambda x: x <= upper_limit and x >= lower_limit,combination
                    )))

    output = ''
    for target in targets:
        if target in posibilities:
            output += 'T'
        else:
            output += 'F'

    print(output)