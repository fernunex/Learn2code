# Problem name: CCC '11 S1 - English or French?
# Code: ccc11s1
# Link: https://dmoj.ca/problem/ccc11s1

n_lines = int(input())
t_cout = 0
s_count = 0

for _ in range(n_lines):
    line = input()
    t_cout = t_cout + line.count('t') + line.count('T')
    s_count = s_count + line.count('s') + line.count('S')

if t_cout > s_count:
    print('English')
else:
    print('French')