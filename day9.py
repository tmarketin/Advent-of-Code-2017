import re

test_stream = r'<{o"i!a,<{i<a>'

def load_stream(fname):
    with open(fname, 'r') as fp:
        s = fp.readline()
    return s

def EliminateGarbage(strr):
    a = re.sub(r'!.', '', strr)
    return re.sub(r'<.*?>', '', a)

def part1(instream):
    strr = EliminateGarbage(instream)
    total_sum = 0
    counter = 0
    for a in strr:
        if(a == '{'):
            counter = counter + 1
            total_sum = total_sum + counter
        if(a == '}'):
            counter = counter - 1
    return total_sum

def part2(strr):
    strr = re.sub(r'!.', '', strr)
    l1 = len(strr)
    nb = strr.count('>')
    strr = EliminateGarbage(strr)
    l2 = len(strr)
    return (l1 - l2) - 2*nb

print('Part 1: ', part1(load_stream('day9.dat')))
print('Part 2: ', part2(load_stream('day9.dat')))
