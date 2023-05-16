# Problem name: WC '18 Contest 3 J1 - An Honest Day's Work
# Code: wc18c3j1
# Link: https://dmoj.ca/problem/wc18c3j1

liters_paint = int(input())
liters_bottlecap = int(input())
pokedollars_for_each = int(input())

total_money = (liters_paint // liters_bottlecap) * pokedollars_for_each + (liters_paint % liters_bottlecap)

print(total_money)