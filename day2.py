def part1(fname):
    with open(fname, 'r') as fp:
        sdiff = 0
        for line in fp:
            l = line.strip().split()
            mmin = int(l[0])
            mmax = int(l[0])
            for item in l:
                if(int(item) > mmax):
                    mmax = int(item)
                if(int(item) < mmin):
                    mmin = int(item)
            sdiff = sdiff + mmax - mmin
    return(sdiff)

def part2(fname):
    with open(fname, 'r') as fp:
        checksum = 0
        for line in fp:
            l = sorted([int(x) for x in line.strip().split()], reverse = True)
            for outer in range(0, len(l) - 1):
                for inner in range(outer + 1, len(l)):
                    if(l[outer] % l[inner] == 0):
                        checksum = checksum + l[outer]/l[inner]
    return checksum
            
            

print('Part 1: ',part1('day2.dat'))
print('Part 2: ',part2('day2.dat'))