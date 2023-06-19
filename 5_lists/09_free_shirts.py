# Problem name: ECOO '19 R1 P1 - Free Shirts
# Code: ecoo19r1p1
# Link: https://dmoj.ca/problem/ecoo19r1p1

for _ in range(10):
    inputs = input().split()

    t_shirts = int(inputs[0])
    events = int(inputs[1])
    days = int(inputs[2])

    schedule_events = input().split()

    for i in range(len(schedule_events)):
        schedule_events[i] = int(schedule_events[i])

    clean_t_shirts = t_shirts
    laundry = 0
    event_t_shirt = 0

    for i in range(1, days + 1):

        if clean_t_shirts == 0:
            laundry += 1
            clean_t_shirts = t_shirts + event_t_shirt
        
        clean_t_shirts -= 1

        if i in schedule_events:
            new_t_shirts = schedule_events.count(i)
            event_t_shirt += new_t_shirts
            clean_t_shirts += new_t_shirts
        
    print(laundry)