# Problem name: CCC '00 S1 - Slot Machines
# Code: ccc00s1
# Link: https://dmoj.ca/problem/ccc00s1

quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

machine = 0
plays = 0

while quarters >= 1:
    quarters = quarters - 1

    if machine % 3 == 0:
        first += 1
        if first % 35 == 0:
            first = 0
            quarters += 30
    elif machine % 3 == 1:
        second += 1
        if second % 100 == 0:
            second = 0
            quarters += 60
    else:
        third += 1
        if third % 10 == 0:
            third = 0
            quarters += 9
    
    machine += 1
    plays += 1

print(f'Martha plays {plays} times before going broke.')