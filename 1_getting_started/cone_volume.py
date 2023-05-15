# Problem name: DMOPC '14 Contest 5 P1 - Core Drill 
# Code: dmopc14c5p1
# Link: https://dmoj.ca/problem/dmopc14c5p1

PI = 3.141592653589793

radius = int(input())
height = int(input())

volume = (PI * radius ** 2 * height) / 3

print(volume)