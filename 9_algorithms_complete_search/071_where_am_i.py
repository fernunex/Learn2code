# Problem name:
# USACO 2019 December Contest, Bronze
# Problem 2. Where Am I?

# Link: http://usaco.org/index.php?page=viewproblem2&cpid=964

input_file = open('whereami.in', 'r')
output_file = open('whereami.out', 'w')

N = int(input_file.readline())
string = input_file.readline()


k = 1
unique = False
while k < N and unique != True:
    for i in range(N - k + 1):
        unique = True
        if string[i:k + i] in string[i+1:]:
            unique = False
            break
    k += 1

# print(k - 1)
output_file.write(f'{k - 1}\n')

input_file.close()
output_file.close()