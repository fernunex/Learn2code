# Problem name: COCI '20 Contest 1 #1 Patkice
# Code: coci20c1p1
# Link: https://dmoj.ca/problem/coci20c1p1

def follow_path(r, s, map_sea):
    """
    r y s are integers where the ducks start the travel
    map_sea is a grid of the map of ocean currents

    Retrun length of the path or None if there is no path.
    """
    way = 0
    while True:
        next_direction = map_sea[r][s]
        if next_direction == '.' or next_direction == 'o':
            return None
        elif next_direction == '^':
            r -= 1
            way += 1
        elif next_direction == 'v':
            r += 1
            way += 1
        elif next_direction == '>':
            s += 1
            way += 1
        elif next_direction == '<':
            s -= 1
            way += 1
        else:
            return way

# Main Paracuat
DIRECTIONS = '^v><x'

import sys
input = sys.stdin.readline

row, s = [int(x) for x in input().strip().split()]

map_sea = []
for i in range(row):
    lst = input().strip()
    if 'o' in lst:
        index = lst.index('o')
        ini_r = i
        ini_s = index

    map_sea.append(lst)


paths = []
min_distance = row * s

# Calculating paths
north_path = follow_path(ini_r - 1, ini_s, map_sea)
south_path = follow_path(ini_r + 1, ini_s, map_sea)
east_path = follow_path(ini_r, ini_s + 1, map_sea)
west_path= follow_path(ini_r, ini_s - 1, map_sea)



# Going North
if north_path != None and north_path <= min_distance:
    if north_path < min_distance:
        paths = []
        min_distance = north_path
    paths.append('N')


# Going South
if south_path != None and south_path <= min_distance:
    if south_path < min_distance:
        paths = []
        min_distance = south_path
    paths.append('S')


# Going East
if east_path != None and east_path <= min_distance:
    if east_path < min_distance:
        paths = []
        min_distance = east_path
    paths.append('E')


# Going west
if west_path != None and west_path <= min_distance:
    if west_path < min_distance:
        paths = []
        min_distance = west_path
    paths.append('W')

if paths:
    paths.sort()
    print(':)')
    print(paths[0])
else:
    print(':(')