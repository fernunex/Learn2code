# Problem name: CCC '13 J1 - Next in line
# Code: ccc13j1
# Link: https://dmoj.ca/problem/ccc13j1

age_youngest = int(input())
age_middle = int(input())

difference = age_middle - age_youngest

age_older = age_middle + difference

print(age_older)