# Problem name: USACO 2019 December Contest, Bronze Problem 1. Cow Gymnastics
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=963

def read_records(input_file):
    """
    input_file is a open file
    return a list of the records of cows
    """
    cows = []
    for record in input_file:
        line = record.split()
        for i in range(len(line)):
            line[i] = int(line[i])
        cows.append(line)
    return cows

def count_consistent_cows(cows_records):
    """
    cows_records is a matrix, has k gymnastic-records for n cows
    count how many cow are consistent, for a consistent pair of cows
    one need to be always better than the other in all records

    return how many consistent pair of cows are
    """
    consistent_cows = 0
    for i in range(1, len(cow_records[0]) + 1):
        for k in range(1, len(cow_records[0]) + 1):
            if i != k:
                consistent = True
                l = 0
                while l < len(cows_records) and consistent:
                    record = cows_records[l]
                    if  k not in record[record.index(i) + 1:]:
                        consistent = False
                    else:
                        l += 1
                if consistent:
                    consistent_cows += 1
    return consistent_cows


# Main
input_file = open('gymnastics.in', 'r')
output_file = open('gymnastics.out', 'w')

# Read Cows
line = input_file.readline().split()
k_records = int(line[0])
n_cows = int(line[1])

cow_records = read_records(input_file)

# Count consistent pairs
consistent_pairs = count_consistent_cows(cow_records)

# Write output
output_file.write(str(consistent_pairs))

input_file.close()
output_file.close()