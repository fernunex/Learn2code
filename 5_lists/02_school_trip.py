# Problem name: ECOO '17 R1 P1 - Munch 'n' Brunch
# Code: ecoo17r1p1
# Link: https://dmoj.ca/problem/ecoo17r1p1

YEAR_COSTS = [12,10, 7, 5]

for _ in range(10):
    cost_trip = int(input())
    proportions_students = input().split()
    number_students = int(input())

    # Converting to float
    proportions_students  = list(map(lambda x: float(x), proportions_students))

    # Number of students per year
    students_per_year = list(map(lambda x: int(x * number_students), proportions_students))

    # Completing the students left
    uncounted = number_students - sum(students_per_year)
    students_per_year[students_per_year.index(max(students_per_year))] += uncounted

    # Calculating money raised
    money_raised = sum(list(map(lambda x, y: x * y, students_per_year, YEAR_COSTS)))

    # Checking if there is more money needed
    if money_raised / 2 < cost_trip:
        print('YES')
    else:
        print('NO')