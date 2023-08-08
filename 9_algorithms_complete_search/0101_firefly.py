# Problem name: COCI '06 Regional #3 Firefly
# Code: crci06p3
# Link: https://dmoj.ca/problem/crci06p3


# Too slow
# Main
# N, H = [int(x) for x in input().split()]


# obstacles = dict()
# for i in range(N):
#     # stalagmites (rising from the floor)
#     if i % 2 == 0:
#         pilar = {x for x in range(1, int(input()) + 1)}
#         for y in pilar:
#             if y not in obstacles:
#                 obstacles[y] = 1
#             else:
#                 obstacles[y] += 1
#     else:
#         pilar = {x for x in range(H + 1 - int(input()), H + 1)}
#         for y in pilar:
#             if y not in obstacles:
#                 obstacles[y] = 1
#             else:
#                 obstacles[y] += 1

# # print(obstacles)

# total = N
# num = 0
# for level in range(1, H + 1):
#     colisions = obstacles[level]
#     # print(colisions)
#     if colisions <= total:
#         if colisions == total:
#             num += 1
#         else:
#             num = 1
#             total = colisions

# print(f"{total} {num}")

#################################3

## TOO SLOW

# def count_colisions(level, obstacles):
#     total = 0
#     for obstacle in obstacles:
#         if level >= obstacle[0] and level <= obstacle[1]:
#             total += 1
#     return total

# # Main
# N, H = [int(x) for x in input().split()]


# obstacles = list()
# for i in range(N):
#     # stalagmites (rising from the floor)
#     if i % 2 == 0:
#         obstacles.append((1, int(input())))
#     else:
#         obstacles.append((H + 1 - int(input()), H))

# # print(obstacles)

# total = N
# num = 0
# for level in range(1, H + 1):
#     colisions = count_colisions(level, obstacles)
#     # print(colisions)
#     if colisions <= total:
#         if colisions == total:
#             num += 1
#         else:
#             num = 1
#             total = colisions

# print(f"{total} {num}")

################
# from bisect import bisect_left, bisect_right

# def count_coisions(level, obstacles):
#     i_0 = bisect_left(obstacles, level)
#     i_1 = bisect_right(obstacles, level)
#     return i_1 - i_0

# # Main
# N, H = [int(x) for x in input().split()]


# obstacles = list()
# for i in range(N):
#     # stalagmites (rising from the floor)
#     if i % 2 == 0:
#         obstacles += [x for x in range(1, int(input()) + 1)]
#     else:
#         obstacles += [x for x in range(H + 1 - int(input()), H + 1)]

# obstacles.sort()
# # print(obstacles)

# total = N
# num = 0
# for level in range(1, H + 1):
#     colisions = count_coisions(level, obstacles)
#     # print(colisions)
#     if colisions <= total:
#         if colisions == total:
#             num += 1
#         else:
#             num = 1
#             total = colisions

# print(f"{total} {num}")


#############################

from bisect import bisect_left, bisect_right

def count_coisions(level, obstacles):
    """
    level is an integer
    obstacles are two lists sorted and contain the 
    levels in which the obstacles are:
    Example [[1,2,3,3,3,4],[2,4,4,4,5]]

    Retrun how many obstacles are destroyed if that level
    is chosen.
    """

    # Stalagmites
    destroyed_stalagmites = len(obstacles[0]) - bisect_left(obstacles[0], level)

    # Stalactites
    destroyed_stalactites = bisect_right(obstacles[1], level)
    return destroyed_stalagmites + destroyed_stalactites

# Main
N, H = [int(x) for x in input().split()]


obstacles = [[],[]]
for i in range(N):
    # stalagmites (rising from the floor)
    if i % 2 == 0:
        obstacles[0].append(int(input()))
    # stalactites (hanging form the celing)
    else:
        obstacles[1].append(H + 1 - int(input()))

obstacles[0].sort()
obstacles[1].sort()

# print(obstacles)

total = N
num = 0
for level in range(1, H + 1):
    colisions = count_coisions(level, obstacles)
    # print(colisions)
    if colisions <= total:
        if colisions == total:
            num += 1
        else:
            num = 1
            total = colisions

print(f"{total} {num}")