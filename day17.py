test_step = 3
puzzle_step = 363

def part1(step, num):
    ll = [0]
    pos = 0
    val = 1
    while(val < num + 1):
        pos = (pos + step) % len(ll)
        ll.insert(pos + 1, val)
        pos = pos + 1
        val = val + 1
    return pos + 1, ll[pos + 1], ll.index(0), ll[ll.index(0) + 1]

def part2(step, num):
    pos = 0
    val = 1
    res = 0
    while(val < num + 1):
        pos = (pos + step) % val
        if(pos == 0):
            res = val
        pos = pos + 1
        val = val + 1
    return res

print('Part 1: ', part1(puzzle_step, 2017))
print('Part 2: ', part2(puzzle_step, 50000000))