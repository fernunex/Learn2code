# Problem name: CCC '06 J1 - Canadian Calorie Counting
# Code: ccc18j1
# Link: https://dmoj.ca/problem/ccc18j1

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

# Telemarketer number: first digit 8 or 9, fourth digit 8 or 9
# second digit and third digit are same
if ((num_1 == 8 or num_1 == 9) and
    (num_4 == 8 or num_4 == 9) and
    (num_2 == num_3)):
    print('ignore')
else:
    print('answer')
    