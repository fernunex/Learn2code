# Problem name:COCI '11 Contest 5 #2 Eko
# Code: coci11c5p2
# Link: https://dmoj.ca/problem/coci11c5p2

# # Fast input/output
from bisect import bisect_right
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))
# print(trees)
trees.sort()

recolected = 0
cut_height = trees[-1]
last_index = 0

while recolected < M:
    cut_height -= 1
    recolected += N - bisect_right(trees, cut_height)
    # print(recolected)

# print("***")
print(cut_height)

# Complexity O(nLog(n))