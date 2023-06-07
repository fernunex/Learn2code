# Problem name: ECOO '15 R1 P1 - When You Eat Your Smarties

# Code: ecoo15r1p1
# Link: https://dmoj.ca/problem/ecoo15r1p1

# handful = 7 Smarties
# 13s per handful non-red
# 16s per One Smartie Red

for _ in range(10):
    orange = 0
    blue = 0 
    green = 0
    yellow = 0
    pink = 0
    violet = 0
    brown = 0
    red = 0

    seconds = 0
    smartie_actual = ''

    while smartie_actual != 'end of box':
        smartie_actual = input()

        if smartie_actual == 'orange':
            orange = orange + 1
        elif smartie_actual == 'blue':
            blue = blue + 1
        elif smartie_actual == 'green':
            green = green + 1
        elif smartie_actual == 'yellow':
            yellow = yellow + 1
        elif smartie_actual == 'pink':
            pink = pink + 1
        elif smartie_actual == 'violet':
            violet = violet + 1
        elif smartie_actual == 'brown':
            brown = brown + 1
        elif smartie_actual == 'red':
            red = red + 1

    handfuls = ((orange+6) // 7 + (blue+6) // 7 + (green+6) // 7 +
                (yellow+6) // 7 + (pink+6) // 7 + (violet+6) // 7 +
                + (brown+6) // 7)

    print(handfuls * 13 + red * 16)