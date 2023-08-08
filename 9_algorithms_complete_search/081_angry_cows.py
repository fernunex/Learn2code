# Problem name:
# USACO 2016 January Contest, Bronze
# Problem 2. Angry Cows

# Link: http://usaco.org/index.php?page=viewproblem2&cpid=592

def last_bomb_in_radius(positions, initial, max_radius):
    """
    positions is the a list with the positions of bale
    must be sorted.
    initial is the bale at t = 0
    max_radius is the bale at maximum radius at t = n

    Return the bale near to maximum radius
    """
    for i in range(max_radius, initial - 1, -1):
        if i in positions:
            return i

def last_bomb_in_radius_rev(positions, initial, max_radius):
    """
    positions is the a list with the positions of bale
    must be sorted.
    initial is the bale at t = 0
    max_radius is the bale at maximum radius at t = n

    Return the bale near to maximum radius
    """
    for i in range(max_radius, initial + 1):
        if i in positions:
            return i


def count_chain_reaction(start, positions: list):
    """
    start is the index of the first bale to detonate.
    positions is the a list with the positions of bale
    must be sorted.

    Return the number of bales exploded.
    """
    
    # Right explosion
    in_range = True
    t = 0
    initial = positions[start]
    while start + t < len(positions) and in_range:
        max_radius = initial + t + 1
        last_bomb = last_bomb_in_radius(positions, initial, max_radius)
        if last_bomb != initial:
            # print(f"Explode at {initial}, max radius: {max_radius}, last explode: {last_bomb}")
            initial = last_bomb
            t += 1
        else:
            in_range = False
    
    right_explosions = (positions[start: positions.index(last_bomb) + 1])
    # print(right_explosions)

    # Left Explosion
    in_range = True
    t = 0
    initial = positions[start]
    while start + t >= 0 and in_range:
        max_radius = initial - t - 1
        last_bomb = last_bomb_in_radius_rev(positions, initial, max_radius)
        if last_bomb != initial:
            # print(f"Explode at {initial}, max radius: {max_radius}, last explode: {last_bomb}")
            initial = last_bomb
            t += 1
        else:
            in_range = False
    
    left_explosions = (positions[positions.index(last_bomb): start])
    # print(left_explosions)

    return (len(right_explosions) + len(left_explosions))




# Main
input_file = open('angry.in', 'r')
output_file = open('angry.out', 'w')

N = int(input_file.readline())

positions = []
for _ in range(N):
    positions.append(int(input_file.readline()))

positions.sort()

total = 0
for i in range(N):
    explosions = count_chain_reaction(i, positions)
    if explosions > total:
        total = explosions

# print(total)
output_file.write(str(total))

input_file.close()
output_file.close()