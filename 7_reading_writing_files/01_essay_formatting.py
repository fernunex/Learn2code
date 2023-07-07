# Problem name: USACO 2020 January Contest, Bronze Problem 1. Word Processor
# Code: 
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=987

input_file = open('word.in', 'r') # for test use 'word_test_for_01.in'
output_file = open('word.out', 'w')

limit_char = int(input_file.readline().rstrip().split()[1])

words = input_file.readline().rstrip().split()
current_line = 0
out_str = ''

for word in words:
    if len(word) + current_line <= limit_char:
        out_str += ' ' + word
        current_line += len(word)
    else:
        out_str += '\n' + word
        current_line = len(word)

output_file.write(out_str[1:])

input_file.close()
output_file.close()