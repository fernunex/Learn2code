# Problem name: COCI '07 Regional #1 Platforme
# Code: crci07p1
# Link: https://dmoj.ca/problem/crci07p1

def intersection_pilar_w_platform(limits: list[int], place_pilar: float) -> bool:
    """Check if a pilar is between two limits

    Args:
        limits (list[int]): at index 0 needs the lower limit and at index 1 needs the higher limit
        place_pilar (float): the place where the pilar is

    Returns:
        bool: True if the place of the pilar is between the limits, False otherwise
    """

    if place_pilar > limits[0] and place_pilar < limits[1]:
        return True
    return False


def calculate_pilar(platfoms_below: list[list[int]], place_pilar: float, altitude: int) -> int:
    """Calculate the lenght of the pilar whether it intersect with other platform or not

    Args:
        platfoms_below (list[list[int]]): list of plataforms below the current platform
        place_pilar (float): the place where the pilar is
        altitude (int): altitude of the platform

    Returns:
        int: the lenght of the pilar to the floor or the platform it intersects
    """
    lenght_pilar = altitude

    i = len(platfoms_below) - 1

    if i == -1:
        return lenght_pilar
    
    while i >= 0:
        platform_just_below = platfoms_below[i]
        limits = platform_just_below[1:]

        if intersection_pilar_w_platform(limits, place_pilar):
            return lenght_pilar - platform_just_below[0]
        i -= 1
    return lenght_pilar

# Main

# Todo: Read Input
n_platforms = int(input())

platforms = []
for _ in range(n_platforms):
    platform = input().split()
    platform = list(map(lambda x: int(x), platform))
    platforms.append(platform)

# Todo: Sort by height
platforms.sort()

# Todo: Calculate sum of pilars
pilars = []

for i in range(len(platforms)):
    altitude = platforms[i][0]
    place_left_pilar = platforms[i][1] + 0.5
    place_right_pilar = platforms[i][2] - 0.5
    platforms_below = platforms[:i]

    length_left_pilar = calculate_pilar(platforms_below, place_left_pilar, altitude)
    length_right_pilar = calculate_pilar(platforms_below, place_right_pilar, altitude)

    pilars.append([length_left_pilar, length_right_pilar])

# Print sum pilars
sum_pilars = 0
for set_pilars in pilars:
    sum_pilars += sum(set_pilars)

print(sum_pilars)