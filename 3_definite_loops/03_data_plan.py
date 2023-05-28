# Problem name: COCI '16 Contest 1 #1 Tarifa
# Code: coci16c1p1
# Link: https://dmoj.ca/problem/coci16c1p1


megabytes_monthly = int(input())
months = int(input())

mb_used = 0

for _ in range(months):
    mb_used_month = int(input())
    mb_used += mb_used_month

print(megabytes_monthly * (months + 1) - mb_used)

