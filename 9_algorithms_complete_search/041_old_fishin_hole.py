# Problem name: CCC '09 J2 - Old Fishin' Hole
# Code: ccc09j2
# Link: https://dmoj.ca/problem/ccc09j2

def combinations_generator(value, limit_points):
    combinations = set()
    i = 0
    while i * value <= limit_points:
        combinations.add(i)
        i += 1
    return combinations


# MAIN
import sys
input = sys.stdin.readline

trout_value = int(input())
pike_value = int(input())
pickerel_value = int(input())
limit_points = int(input())

# Generate combinations for each fish
comb_trout_single = combinations_generator(trout_value, limit_points)
comb_pike_single = combinations_generator(pike_value, limit_points)
comb_pickerel_single = combinations_generator(pickerel_value, limit_points)


# Combining all combinations
total = 0

for comb1 in comb_trout_single:
    if (comb1 * trout_value) < limit_points:
        for comb2 in comb_pike_single:
            if (comb1 * trout_value + comb2 * pike_value) < limit_points:
                for comb3 in comb_pickerel_single:
                    if (comb1 + comb2 + comb3) != 0 and (
                        (comb1 * trout_value +
                        comb2 * pike_value +
                        comb3 * pickerel_value) <= limit_points):

                        print(f"{comb1} Brown Trout, {comb2} Northern Pike, {comb3} Yellow Pickerel")
                        total += 1
            elif (comb1 * trout_value + comb2 * pike_value) == limit_points:
                print(f"{comb1} Brown Trout, {comb2} Northern Pike, 0 Yellow Pickerel")
                total += 1
    else:
        print(f"{comb1} Brown Trout, 0 Northern Pike, 0 Yellow Pickerel")
        total += 1


print(f"Number of ways to catch fish: {total}")