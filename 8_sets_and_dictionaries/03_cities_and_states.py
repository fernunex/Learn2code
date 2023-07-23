# Problem name: USACO 2016 December Contest, Silver Problem 2. Cities and States
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=667

input_file = open('citystate.in', 'r')
output_file = open('citystate.out', 'w')

N = int(input_file.readline())

city_state_combo = {}

for _ in range(N):
    lst = input_file.readline().split()
    city = lst[0][:2]
    state = lst[1]
    if city != state:
        combo = city + state
        if combo not in city_state_combo:
            city_state_combo[combo] = 1
        else:
            city_state_combo[combo] += 1
    
total = 0
for combo in city_state_combo:
    flipped_combo = combo[2:] + combo[:2]
    if flipped_combo in city_state_combo:
        total += city_state_combo[combo] * city_state_combo[flipped_combo]

output_file.write(str(total//2))

input_file.close()
output_file.close()