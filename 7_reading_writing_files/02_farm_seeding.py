# Problem name: 
# USACO 2019 February Contest, Bronze
# Problem 2. The Great Revegetation
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=916&lang=en#

def read_cows(file):
    """
    file is a file open for reading; cow information is next to read.

    Read the cows' favorite pasture from file.
    Return a list of each cow's two favorite pastures;
    each value in the list is a list of two values giving the
    favorite pasture for one cow.
    """
    favorites = []
    for cow in file:
        lst = cow.rstrip().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favorites.append(lst)
    return favorites

def cows_with_favorite(favorites, pasture):
    """
    favorites is a list of favorite pastures, as returned by read_cows.
    pasture is a pasture number.

    Return a list of cows that care about pasture.
    """

    counter = 0
    i = 0
    cows = []
    while counter < 3 and i < len(favorites):
        if pasture in favorites[i]:
            cows.append(i)
            counter += 1
        i += 1
    return cows

def types_used(favorites, cows, pasture_types):
    """
    favorites is a list of favorites pastures, as returned by read_cow.
    cows is a list of cows.
    pasture_types is a list of grass types already seeded.

    Return a list of the grass types already used by cows.
    """

    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]

        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])

        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used

def smallest_available(eliminated):
    """
    used is a list of used grass types.

    Return the smallest-numbered grass type that is not in used.
    """
    grass_type = 1
    while True:
        if grass_type not in eliminated:
            return grass_type
        grass_type += 1

def write_pastures(output_file, pastures):
    """
    output_file is a file open for writing.
    pastures is a list of integer grass types.

    Output pastures to output_file
    """
    for pasture in pastures:
        output_file.write(str(pasture))


# Main Program

input_file = open('revegetate.in', 'r')
output_file = open('revegetate.out', 'w')

# Read input
lst = input_file.readline().rstrip().split()
num_pastures = int(lst[0])
num_cows = int(lst[1])
favorites = read_cows(input_file)

pasture_types = [0]

for i in range(1, num_pastures + 1):
    # Identify cows that care about pasture
    cows = cows_with_favorite(favorites, i)

    # Eliminate grass type for pasture
    eliminated = types_used(favorites, cows, pasture_types)

    # Choose smallest-numbered grass type for pasture
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

# Write output
pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()