# Problem name: USACO 2017 US Open Contest, Bronze Problem 2. Bovine Genomics
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=736

def read_genomes(input_file, n_cows):
    """
    input_file is a open file that contais information about cows
    n_cows is the number of spotty cows, then another n_cows is the number
    of plain cows (the total lines are n_cows * 2)

    return two list: the first with information about spotty cows and the last with 
    information about plain cows (genomes of the cows)
    """
    grid_spotty = []
    grid_plain = []
    
    for _ in range(n_cows):
        grid_spotty.append(input_file.readline().rstrip())
    
    for _ in range(n_cows):
        grid_plain.append(input_file.readline().rstrip())

    return [grid_spotty, grid_plain]

def gen_in_plain(gen, cows_plain, index_location, n_cows):
    """
    check if the gen is on the any n_cows at index_location in the cows_plain list.

    return True if there is one coincidende
    """
    j = 0
    while j < n_cows:
        if gen == cows_plain[j][index_location]:
            return True
        j += 1
    return False


def count_potentially_locations(cows_spotty, cows_plain, n_cows, m_genomes):
    """
    cow_spotty is a list with the genome of the n_cows spotty cows
    cows_plain is a list with the genome of the n_cows plain cows
    m_genomes is the number of positions or genes that contains each cow

    return the number of potentially positions in the genome that could potentially explain spottiness
    """

    locations = 0
    for i in range(m_genomes):
        spotty_potential = True
        j = 0
        while spotty_potential and j < n_cows:
            gen = cows_spotty[j][i]
            if gen_in_plain(gen, cows_plain, i, n_cows):
                spotty_potential = False
            j += 1
        
        if spotty_potential:
            locations += 1
    return locations

# Main
input_file = open('cownomics.in', 'r')
output_file = open('cownomics.out', 'w')

# Read Input
line = input_file.readline().split()
n_cows = int(line[0])
m_genomes = int(line[1])

grid_genomes = read_genomes(input_file, n_cows)

# Check spotiness
no_of_positions = count_potentially_locations(grid_genomes[0], grid_genomes[1], n_cows, m_genomes)

# Write input
output_file.write(str(no_of_positions))

input_file.close()
output_file.close()