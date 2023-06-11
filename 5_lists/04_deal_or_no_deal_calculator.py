# Problem name: CCC '07 J3 - Deal or No Deal Calculator
# Code: ccc07j3
# Link: https://dmoj.ca/problem/ccc07j3

brief_cases = [100, 500, 1000, 5000, 10000, 25000, 
                50000, 100000, 500000, 1000000]

n = int(input())

for _ in range(n):
    brief_case_opened = int(input())
    brief_cases[brief_case_opened - 1] = 0

banker_offer = int(input())
average = sum(brief_cases) / (len(brief_cases) - n)

if banker_offer > average:
    print('deal')
else:
    print('no deal')

