# Problem name: ECOO '18 R1 P2 - Rue's Rings
# Code: ecoo18r1p2
# Link: https://dmoj.ca/problem/ecoo18r1p2

for _ in range(10):
    number_of_routes = int(input())
    routes = []

    for _ in range(number_of_routes):
        route = input().split()
        route = list(map(lambda x: int(x), route))
        routes.append(route)

    minimum = 70000

    for route in routes:
        min_of_current_route = min(route[2:])
        if min_of_current_route < minimum:
            minimum = min_of_current_route

    id_of_minmums = []

    for route in routes:
        if minimum in route[2:]:
            id_of_minmums.append(route[0])

    id_of_minmums.sort()

    string_of_ids = ''

    for i in id_of_minmums:
        string_of_ids = string_of_ids + str(i) + ','

    print(f"{minimum} {{{string_of_ids[:-1]}}}" )