import numpy as np

test_data = 'flqrgnkx'
input_data = 'wenycdww'

MAXDIM = 128

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

def SingleKnotHash(ll, lengths, pos, skip):
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
        res, pos, skip = SingleKnotHash(inlist, lengths, pos, skip)
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

def FullKnotHash(ss):
    return ConvertToHex(DenseHash(SparseHash(list(range(256)),GeneratePart2Input(ss))))

def part1(ss):
    counter = 0
    for row in range(MAXDIM):
        hash_input = ss + '-' + str(row)
        hh = FullKnotHash(hash_input)
        binhh = str(bin(int(hh, 16))[2:].zfill(MAXDIM))
        counter = counter + binhh.count('1')
    return counter

def FindNextGroup(a):
    for r in range(MAXDIM):
        for c in range(MAXDIM):
            if(a[r, c] == 1):
                return r, c
    return -1, -1

def EliminateGroup(a, rstart, cstart):
    que = [[rstart, cstart]]
    while(len(que) > 0):
        cr = que[0][0]
        cc = que[0][1]
        a[cr, cc] = 0
        if(cr > 0 and a[cr - 1, cc] == 1):
            que.append([cr-1, cc])
        if(cr < MAXDIM - 1 and a[cr + 1, cc] == 1):
            que.append([cr + 1, cc])
        if(cc > 0 and a[cr, cc - 1] == 1):
            que.append([cr, cc - 1])
        if(cc < MAXDIM - 1 and a[cr, cc + 1] == 1):
            que.append([cr, cc + 1])
        que = que[1:]
    
    return

def part2(ss):
    ar = np.zeros([MAXDIM, MAXDIM])
    for row in range(MAXDIM):
        hh = FullKnotHash(ss + '-' + str(row))
        binhh = str(bin(int(hh, 16))[2:].zfill(MAXDIM))
        for col in range(MAXDIM):
            ar[row, col] = binhh[col]
    
    num_groups = 0
    while(np.any(ar > 0)):
        rpos, cpos = FindNextGroup(ar)
        if(rpos == -1 and cpos == -1):
            break # should never happen
        num_groups = num_groups + 1
        EliminateGroup(ar, rpos, cpos)
    
    return num_groups

print(part1(input_data))
print(part2(input_data))