# Problem name: DMOPC '17 Contest 4 P1 - Ribbon Colouring Fun
# Code: dmopc17c4p1
# Link: https://dmoj.ca/problem/dmopc17c4p1

n, q = [int(x) for x in input().split()]

strokes = []
for _ in range(q):
    strokes.append([int(x) for x in input().split()])

# O(q*log(q))
strokes.sort()

rightmost = 0
blue = 0

for stroke in strokes:
    start = stroke[0]
    end = stroke[1]

    if start <= rightmost:
        if end > rightmost:
            blue += end - rightmost
            rightmost = end
    else:
        blue += end - start
        rightmost = end

print(n - blue, blue)