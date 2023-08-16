# Problem name: DMOPC '20 Contest 1 P2 - Victor's Moral Dilemma
# Code: dmopc20c1p2
# Link: https://dmoj.ca/problem/dmopc20c1p2

# fast input/ output
import sys
input = sys.stdin.readline
print = sys.stdout.write


# N, D = [int(x) for x in input().split()]
N, D = map(int, input().split())

# trolleys = [int(x) for x in input().split()]
trolleys = list(map(int, input().split()))

for _ in range(D):
    ni = int(input())
    F = trolleys[:ni]
    S = trolleys[ni:]
    # print(f"F= [{F}]")
    # print(f"S= [{S}]")
    f_sum = sum(F)
    s_sum = sum(S)

    if f_sum >= s_sum:
        print(str(f_sum) + '\n')
        trolleys = S
    else:
        print(str(s_sum) + '\n')
        trolleys = F