testdata = [0, 2, 7, 0]
indata = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]

def part12(ll):
    count = 0
    visited = []
    while(ll not in visited):
        visited.append(list(ll))
        count = count + 1
        idx = ll.index(max(ll))
        val = ll[idx]
        ll[idx] = 0
        while(val > 0):
            idx = (idx + 1) % len(ll)
            ll[idx] = ll[idx] + 1
            val = val - 1
    idx = visited.index(ll)
    return count, count - idx

p1, p2 = part12(indata)
print('Part 1: ',p1)
print('Part 2: ',p2)