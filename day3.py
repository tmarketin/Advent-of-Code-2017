import numpy as np

next_direction = {'s': 'w', 'w': 'n', 'n': 'e', 'e': 's'}

def Coords(num):
    i2 = 1
    while(i2*i2 < num):
        i2 = i2 + 2
    x = int(i2 - 1)/2
    y = -x
    diff = i2*i2 - num
    if(diff > 0):
        x = x - min(diff, i2 - 1)
        diff = diff - min(diff, i2 - 1)
    if(diff > 0):
        y = y + min(diff, i2 - 1)
        diff = diff - min(diff, i2 - 1)
    if(diff > 0):
        x = x + min(diff, i2 - 1)
        diff = diff - min(diff, i2 - 1)
    if(diff > 0):
        y = y - min(diff, i2 - 1)
        diff = diff - min(diff, i2 - 1)
    return int(x), int(y)

def part1(num):
    x, y = Coords(num)
    return abs(x) + abs(y)

def NextStep(x, y, direction):
    if(direction == 's'):
        y = y + 1
    elif(direction == 'w'):
        x = x + 1
    elif(direction == 'n'):
        y = y - 1
    elif(direction == 'e'):
        x = x - 1
    return x, y

def Sum33(x, y, field):
    s = 0
    s = field[y-1,x-1] + field[y-1,x] + field[y-1,x+1]
    s = s + field[y,x-1] + field[y,x] + field[y,x+1]
    s = s + field[y+1,x-1] + field[y+1,x] + field[y+1,x+1]
    return s

def part2(num):
    ndim = 21
    field = np.zeros([ndim, ndim])
    x = int((ndim - 1)/2)
    y = int((ndim - 1)/2)
    field[y, x] = 1
    direction = 's'
    while(field[y, x] < num):
        xtmp, ytmp = NextStep(x, y, next_direction[direction])
        if(field[ytmp, xtmp] < 0.5):
            direction = next_direction[direction]
        x, y = NextStep(x, y, direction)
        field[y, x] = Sum33(x, y, field)
    return int(field[y, x])

print('Part 1: ', part1(347991))
print('Part 2: ', part2(347991))