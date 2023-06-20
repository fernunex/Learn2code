# Problem name: Wesley's Anger Contest 3 Problem 3 - Wesley Plays DDR
# Code: wac3p3
# Link: https://dmoj.ca/problem/wac3p3

S = input()
M = int(input())
C = []
P = []
score = 0

for _ in range(M):
    line = input().split()
    C.append(line[0])
    P.append(int(line[1]))


C_lengths = []
for k in range(len(C)):
    C_lengths.append(len(C[k]))


i = 0

while i < len(S):
    C_lengths_dinamic = C_lengths[:]

    for _ in range(len(C)):
        index_max_combo = C_lengths_dinamic.index(max(C_lengths_dinamic))
        longest_combo = C[index_max_combo]

        if  longest_combo in S[i:i + len(longest_combo)]:
            score += P[index_max_combo]
            i += len(longest_combo) - 1
            break
            

        else:
            C_lengths_dinamic[index_max_combo] = 0

    i += 1

score += len(S)

print(score)