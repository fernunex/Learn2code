# Problem name: Wesley's Anger Contest 6 Problem 2 - Cheap Christmas Lights
# Code: wac6p2
# Link: https://dmoj.ca/problem/wac6p2

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lights = input().split()
lights_on = lights.count('1')

if lights_on > 0:
    all_off = False
    b_changes = list(map(lambda x: int(x) - 1, input().split()))
    switches_acummulated = 0
    # print(b_changes)


    for change in b_changes:
        switches_acummulated += 1

        lights_on += 1 if lights[change] == '0' else -1
        lights[change] = '0' if lights[change] == '1' else '1'


        if switches_acummulated >= lights_on:
            all_off = True
            break

    if all_off:
        print(switches_acummulated)
    else:
        print((lights_on - switches_acummulated) + switches_acummulated) 

else:
    print(0)