import re
import copy
import numpy as np

def load_input(fname):
    retlist = []
    with open(fname, 'r') as fp:
        for line in fp:
            l = re.sub(r'[\>=]', '', line)
            retlist.append(l.strip().split())
    return retlist

def PrintMat(mat):
    for row in mat:
        print(''.join(row))
    print()
    return

def CountOnes(mat):
    cnt = 0
    for row in mat:
        for c in row:
            if(c == '#'):
                cnt = cnt + 1
    return cnt

def StrToMat(s):
    return np.asarray([list(x) for x in s.strip().split('/')])

def MatToStr(mat):
    return '/'.join([''.join(row) for row in mat])

def BuildInput(mat):
    ll = []
    for idx in range(4):
        rmat = np.rot90(mat, idx)
        s = MatToStr(rmat)
        if(s not in ll):
            ll.append(s)

    rmat = np.transpose(mat)
    for idx in range(4):
        rmat = np.rot90(rmat)
        s = MatToStr(rmat)
        if(s not in ll):
            ll.append(s)
    return ll

def ReplacementMatrix(rules, ll):
    for item in ll:
        for rule in rules:
            if(item == rule[0]):
                return StrToMat(rule[1])

def SingleIteration(mat, size, rules):
    if(size % 2 == 0):
        nmat = int(size/2)
        newsize = nmat*3
        subsize = 2
    else:
        nmat = int(size/3)
        newsize = nmat*4
        subsize = 3
    newsubsize = subsize + 1

    newmat = np.array([['.']*newsize for x in range(newsize)])
    for row in range(nmat):
        for col in range(nmat):
            in_list = BuildInput(mat[row*subsize:(row + 1)*subsize, col*subsize:(col + 1)*subsize])
            newmat[row*newsubsize:(row + 1)*newsubsize, col*newsubsize:(col + 1)*newsubsize] = ReplacementMatrix(rules, in_list)

    return newmat, newsize

def part1(mat, size, rules, maxiter):
    for iter in range(maxiter):
        mat, size = SingleIteration(mat, size, rules)
        print('Iteration: ', iter, ', count: ', CountOnes(mat))
    return CountOnes(mat)

init_m = np.asarray([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']])
init_size = 3
rules = load_input('day21.dat')
print('Part 1: ', part1(copy.copy(init_m), init_size, rules, 5))
print('Part 2: ', part1(copy.copy(init_m), init_size, rules, 18))
