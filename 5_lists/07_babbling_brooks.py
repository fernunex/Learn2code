# Problem name: CCC '00 S2 - Babbling Brooks
# Code: ccc00s2
# Link: https://dmoj.ca/problem/ccc00s2

n = int(input())

streams = []

for _ in range(n):
    flow = int(input())
    streams.append(flow)

flag = '0'

while flag != '77':
    flag = input()

    if flag == '99': # split
        index_river = int(input()) - 1
        percentage = int(input()) / 100

        streams.insert(index_river + 1, streams[index_river] * (1 - percentage))
        streams[index_river] = streams[index_river] * percentage

    elif flag == '88': # join
        index_river = int(input()) - 1
        streams[index_river] = streams[index_river + 1] + streams.pop(index_river)


result = ''
for stream in streams:
    result += str(round(stream)) + ' '

print(result[:-1])