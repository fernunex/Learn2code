# Problem name: DMOPC '14 Contest 7 P2 - Tides
# Code: dmopc14c7p2
# Link: https://dmoj.ca/problem/dmopc14c7p2

n_readings = int(input())
readings = input().split()

for i in range(n_readings):
    readings[i] = int(readings[i])

minimum_index = readings.index(min(readings))
maximum_index = readings.index(max(readings))

if minimum_index < maximum_index:
    output = max(readings) - min(readings)

    sequence_increasing = readings[minimum_index:maximum_index]

    for i in range(len(sequence_increasing) - 1):
        if sequence_increasing[i] > sequence_increasing[i + 1]:
            output = 'unknown'

    print(output)

else:
    print('unknown')
