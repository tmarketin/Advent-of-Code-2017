def load_input(fname):
    retval = []
    with open(fname, 'r') as fp:
        for line in fp:
            retval.append(int(line))
    return retval

def part1(ll):
    idx = 0
    count = 0
    while(idx >= 0 and idx < len(ll)):
        ll[idx] = ll[idx] + 1
        idx = idx + ll[idx] - 1
        count = count + 1
    return count

def part2(ll):
    idx = 0
    count = 0
    while(idx >= 0 and idx < len(ll)):
        if(ll[idx] >= 3):
            ll[idx] = ll[idx] - 1
            idx = idx + ll[idx] + 1
        else:
            ll[idx] = ll[idx] + 1
            idx = idx + ll[idx] - 1
        count = count + 1
    return count

print('Part 1: ',part1(load_input('day5.dat')))
print('Part 2: ',part2(load_input('day5.dat')))