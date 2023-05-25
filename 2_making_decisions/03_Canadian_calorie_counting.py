# Problem name: CCC '06 J1 - Canadian Calorie Counting
# Code: ccc06j1
# Link: https://dmoj.ca/problem/ccc06j1

# Inputs
burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

# Counting calories
total_calories = 0

# Burgers
if burger_choice == 1:
    total_calories += 461

elif burger_choice == 2:
    total_calories += 431

elif burger_choice == 3:
    total_calories += 420

else:
    pass

# Side
if side_choice == 1:
    total_calories += 100

elif side_choice == 2:
    total_calories += 57

elif side_choice == 3:
    total_calories += 70

else:
    pass

# Drink
if drink_choice == 1:
    total_calories += 130

elif drink_choice == 2:
    total_calories += 160

elif drink_choice == 3:
    total_calories += 118

else:
    pass

# Dessert
if dessert_choice == 1:
    total_calories += 167

elif dessert_choice == 2:
    total_calories += 266

elif dessert_choice == 3:
    total_calories += 75

else:
    pass

print(f'Your total Calorie count is {total_calories}.')