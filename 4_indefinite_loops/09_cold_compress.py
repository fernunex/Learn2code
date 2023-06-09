# Problem name: CCC '19 J3 - Cold Compress
# Code: ccc19j3
# Link: https://dmoj.ca/problem/ccc19j3


n = int(input())

for _ in range(n):
    encoded = ''
    line = input()
    counter = 0
    occurrence = 0

    while len(line) > counter:
        if counter == (len(line) - 1):
            occurrence += 1
            encoded = encoded + f'{occurrence} {line[counter]}'
            counter+= 1
            
        elif line[counter] == line[counter + 1]:
            occurrence += 1
            counter += 1
        else:
            occurrence += 1
            encoded = encoded + f'{occurrence} {line[counter]} '
            counter += 1
            occurrence = 0

    print(encoded)
