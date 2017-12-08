def part1(fname):
    with open(fname, 'r') as fp:
        num_valid = 0
        for line in fp:
            l = line.strip().split()
            newlist = list(set(l))
            if(len(l) == len(newlist)):
                num_valid = num_valid + 1
    return num_valid

def part2(fname):
    with open(fname, 'r') as fp:
        num_valid = 0
        for line in fp:
            l = [''.join(sorted(x)) for x in line.strip().split()]
            newlist = list(set(l))
            if(len(l) == len(newlist)):
                num_valid = num_valid + 1
    return num_valid

#print('Part 1: ',part1('day4.dat'))
print('Part 2: ',part2('day4.dat'))