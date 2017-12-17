def load_input(fname):
    with open(fname, 'r') as fp:
        for line in fp:
            retval = line.strip().split(',')
    return retval

def swap(a, b, ll):
    tmp = ll[a]
    ll[a] = ll[b]
    ll[b] = tmp
    return

def part1(instructions, ordering):
    lo = len(ordering)
    for inst in instructions:
        if(inst[0] == 's'):
            n = int(inst[1:])
            ordering = ordering[-n:] + ordering[:lo - n]
        if(inst[0] == 'x'):
            el = [int(x) for x in inst[1:].split('/')]
            swap(el[0], el[1], ordering)
        if(inst[0] == 'p'):
            items = [inst[1], inst[3]]
            swap(ordering.index(items[0]), ordering.index(items[1]), ordering)
    return ''.join(ordering)

def part2(instructions, ordering, numrepetitions):
    ll = ordering
    hist = [ll]
    counter = 0
    for x in range(numrepetitions):
        ll = part1(instructions, list(ll))
        counter = counter + 1
        if(ll in hist):
            print(ll)
            print(hist.index(ll), counter)
            break
        hist.append(ll)
    return hist[1000000000 % counter]

instructions = load_input('day16.dat')
print('Part 1: ', part1(instructions, list('abcdefghijklmnop')))
print('Part 2: ', part2(instructions, 'abcdefghijklmnop', 1000))