# Problem name: CCC '18 J3 - Are we there yet?
# Code: ccc18j3
# Link: https://dmoj.ca/problem/ccc18j3

def distances_from_0(distances: list[int]) -> list[int]:
    """Calculate all the distances referenced from 0 city

    Args:
        distances (list[int]): list of distances between two cities

    Returns:
        list[int]: List of distances between all cities against the city 0
    """

    distances_0 = []
    counter = 0

    for num in distances:
        counter += num
        distances_0.append(counter)
    return distances_0


def read_distances() -> list[int]:
    """Read the input of distances

    Returns:
        list[int]: list of the distances between consecutive 
        pairs of consecutive cities and at index 0 the 0 number 
    """
    distances = input()
    distances = distances.split()

    distances.insert(0, 0)
    distances = list(map(lambda x: int(x), distances))

    distances = distances_from_0(distances)

    return distances

def distances_btw_cities(city_number, list_cities) -> list[int]:
    """The distance of all cities against the city at city_number

    Args:
        city_number (_type_): index of the city
        list_cities (_type_): list of real distances (referenced at 0) of all the cities

    Returns:
        list[int]: The calculated distances
    """
    calculated_distance = []

    for i in range(len(list_cities)):
        if i == city_number:
            calculated_distance.append(0)
        else:
            distance = abs(list_cities[city_number] - list_cities[i])
            calculated_distance.append(distance)
    return calculated_distance

def format_int_to_str(list_ints: list[int]) -> str:
    """Format a list of ints to a string of the elements separated by a space

    Args:
        list_ints (list[int]): a list of integers

    Returns:
        str: a single string with all the integer values separated by a space
    """

    string = ''

    for num in list_ints:
        string += str(num) + ' '

    return string[:-1]


# Read input
distances = read_distances()


# Calculate distances and print

for i in range(len(distances)):
    distance_for_city = distances_btw_cities(i, distances)
    distance_for_city = format_int_to_str(distance_for_city)
    print(distance_for_city)