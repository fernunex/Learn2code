# Problem name: COCI '10 Contest 1 #2 Profesor
# Code: coci10c1p2
# Link: https://dmoj.ca/problem/coci10c1p2

# Main
# Fast input/output
import sys
input = sys.stdin.readline

N = int(input())

max_score_1 = 0
max_score_2 = 0
max_score_3 = 0
max_score_4 = 0
max_score_5 = 0

pseudo_1 = 0
pseudo_2 = 0
pseudo_3 = 0
pseudo_4 = 0
pseudo_5 = 0


for _ in range(N):
    desk = input().strip()

    pseudo_1 = pseudo_1 + 1 if "1" in desk else 0
    # pseudo_1 = check_score("1", desk, pseudo_1)
    max_score_1 = max(max_score_1, pseudo_1)

    pseudo_2 = pseudo_2 + 1 if "2" in desk else 0
    max_score_2 = max(max_score_2, pseudo_2)

    pseudo_3 = pseudo_3 + 1 if "3" in desk else 0
    max_score_3 = max(max_score_3, pseudo_3)

    pseudo_4 = pseudo_4 + 1 if "4" in desk else 0
    max_score_4 = max(max_score_4, pseudo_4)

    pseudo_5 = pseudo_5 + 1 if "5" in desk else 0
    max_score_5 = max(max_score_5, pseudo_5)


answers = [
    (max_score_1, 1),
    (max_score_2, 2),
    (max_score_3, 3),
    (max_score_4, 4),
    (max_score_5, 5),

]
answers.sort(reverse=True)

for i in range(4):
    if answers[i][0] != answers[i + 1][0]:
        print(f"{answers[i][0]} {answers[i][1]}")
        break