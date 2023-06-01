# Problem name: CCC '08 J2 - Do the Shuffle
# Code: ccc08j2
# Link: https://dmoj.ca/problem/ccc08j2

button = 0
songs = 'ABCDE'

while button != 4:
    button = int(input())
    presses = int(input())

    for _ in range(presses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ''
for song in songs:
    output = output + song + ' '

print(output[:-1])
