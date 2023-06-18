# Problem name: COCI '18 Contest 2 #1 Preokret
# Code: coci18c2p1
# Link: https://dmoj.ca/problem/coci18c2p1

team_A_points = int(input())
seconds_A = []

for _ in range(team_A_points):
    point = int(input())
    seconds_A.append(point)

team_B_points = int(input())
seconds_B = []

for _ in range(team_B_points):
    point = int(input())
    seconds_B.append(point)

half_time_points = (len(list(filter(lambda x: x <= 1440, seconds_A))) + 
                    len(list(filter(lambda x: x <= 1440, seconds_B))))


turnarounds = 0
winning = ''
score_A = 0
score_B = 0
i = 0
k = 0


for _ in range(team_A_points + team_B_points):

    if k == len(seconds_B):
        score_A += 1
        i += 1
    elif i < len(seconds_A) and seconds_A[i] < seconds_B[k]:
        score_A += 1
        i += 1
    else:
        score_B += 1
        k += 1
        
    if score_A > score_B:
        if winning == 'B':
            turnarounds += 1
        winning = 'A'
    elif score_B > score_A: 
        if winning == 'A':
            turnarounds += 1
        winning = 'B'
    

print(half_time_points)
print(turnarounds)