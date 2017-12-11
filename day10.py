test_input = [3, 4, 1, 5]
day10_input = [130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224]
day10_input_p2 = "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"

def Reverse(ll, pos, length):
    if(pos + length <= len(ll)):
        ll[pos:pos+length] = ll[pos:pos+length][::-1]
    else:
        l1 = len(ll[pos:])
        s = ll[pos:] + ll[:length - l1]
        s = s[::-1]
        ll[pos:] = s[:l1]
        ll[:length - l1] = s[l1:]
    return


def part1(ll, lengths, pos, skip):
    for item in lengths:
        Reverse(ll, pos, item)
        pos = (pos + item + skip) % len(ll)
        skip = skip + 1
    return ll[0]*ll[1], pos, skip

def GeneratePart2Input(s):
    post_list = [17, 31, 73, 47, 23]
    return [ord(x) for x in s] + post_list

def SparseHash(inlist, lengths):
    pos = 0
    skip = 0
    for loop in range(64):
        res, pos, skip = part1(inlist, lengths, pos, skip)
    return inlist

def DenseHash(inlist):
    res = []
    for block in range(16):
        x = inlist[block*16]
        for idx in range(1,16):
            x = x^inlist[block*16 + idx]
        res.append(x)
    return res

def ConvertToHex(inlist):
    s = ''
    for item in inlist:
        t = hex(item)[2:]
        if(len(t) == 1):
            t = '0' + t
        s = s + t
    return s

MAXSIZE = 256

init_list = list(range(MAXSIZE))

init_pos = 0
init_skip = 0
res_part1, init_pos, init_skip = part1(init_list, day10_input, init_pos, init_skip)
print('Part 1: ', res_part1)
print('Part 2: ',ConvertToHex(DenseHash(SparseHash(list(range(MAXSIZE)),GeneratePart2Input(day10_input_p2)))))