# Problem name: CCC '15 J2 - Happy or Sad
# Code: ccc15j2
# Link: https://dmoj.ca/problem/ccc15j2

message = input()

sad_emoticon = message.count(':-(')
happy_emoticon = message.count(':-)')

if (sad_emoticon == 0 and happy_emoticon == 0):
    print('none')
elif sad_emoticon > happy_emoticon:
    print('sad')
elif sad_emoticon < happy_emoticon:
    print('happy')
else:
    print('unsure')