# Problem name: ECOO '18 R1 P1 - Willow's Wild Ride
# Code: ecoo18r1p1
# Link: https://dmoj.ca/problem/ecoo18r1p1


## Not SOLVED 40/50
# for _ in range(10):
#     t_and_n = input().split()
#     T =  int(t_and_n[0])
#     N = int(t_and_n[1])

#     box_shopping = []
#     day_shift = 0
#     days_delayed = 0

#     for _ in range(N):
#         box_shopping.append(input())
    
#     boxes = box_shopping.count('B')

#     if 'B' in box_shopping:  
#         day_shift = box_shopping.index('B')
#         days_delayed = boxes * T + day_shift - N

#         if days_delayed < 0:
#             days_delayed = 0

#         print(days_delayed)

#     else:
#         days_delayed = 0
#         print(days_delayed)


for _ in range(10):
    t_and_n = input().split()
    T =  int(t_and_n[0])
    N = int(t_and_n[-1])

    cat = 0
    for i in range(N):
        day = input()

        if day == 'B':
            cat = cat + T - 1

        else:
            if cat > 0:
                cat = cat - 1

    print(cat)