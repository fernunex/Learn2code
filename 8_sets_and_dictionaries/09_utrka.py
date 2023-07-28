# Problem name: COCI '14 Contest 2 #2 Utrka
# Code: coci14c2p2
# Link: https://dmoj.ca/problem/coci14c2p2

## VERSION SET
# import sys

# input = sys.stdin.readline

# N = int(input())

# contestants = set()
# for i in range((N * 2) - 1):
#     contestant = input()
    
#     if contestant not in contestants:
#         contestants.add(contestant)
#     else: 
#         contestants.remove(contestant)


# print(contestants.pop())

## VERSION DICT
import sys

input = sys.stdin.readline

N = int(input())

contestants = {}

for _ in range(N * 2 - 1):
    contestant = input()
    if contestant not in contestants:
        contestants[contestant] = 1
    else:
        contestants[contestant] += 1

for key in contestants:
    if not contestants[key] % 2 == 0:
        print(key)
        break

## VERSION LIST
# import sys

# input = sys.stdin.readline

# N = int(input())

# contestants = []
# for _ in range(N):
#     cont = input().strip()
#     contestants.append(cont)

# for _ in range(N - 1):
#     cont2 = input().strip()
#     contestants.remove(cont2)

# print(contestants.pop())