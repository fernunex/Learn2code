# Problem name: CCC '11 S2 - Multiple Choice
# Code: ccc11s2
# Link: https://dmoj.ca/problem/ccc11s2

N_lines = int(input())
corrects = 0

answers_student = ''
answers_correct = ''

for _ in range(N_lines):
    answer = input()
    answers_student = answers_student + answer

for _ in range(N_lines):
    answer = input()
    answers_correct = answers_correct + answer

for i in range(N_lines):
    if answers_student[i] == answers_correct[i]:
        corrects += 1

print(corrects)