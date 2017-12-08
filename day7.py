import re
import copy
from collections import Counter

def load_input(fname):
    retlist = {}
    with open(fname, 'r') as fp:
        for line in fp:
            ll = [x for x in re.sub('[()\-\>,]','',line).strip().split()]
            ll[1] = int(ll[1])
            retlist[ll[0]] = ll[1:]
    return retlist

def part1(dd):
    keys = list(dd)
    for item in dd:
        if(len(dd[item]) > 1):
            for t in dd[item][1:]:
                keys.remove(t)
    return keys[0]

def part2(dd, root):
    if(len(dd[root]) == 1):
        return dd[root][0]
    weights = []
    for item in dd[root][1:]:
        weights.append(part2(dd,item))
    if(len(set(weights)) > 1):
        res = Counter(weights)
        for item in res:
            if(res[item] == 1):
                prob_weight = item
        for item in res:
            if(item != prob_weight):
                weight_diff = prob_weight - item
        prob_tower_idx = weights.index(prob_weight)
        prob_tower = dd[root][prob_tower_idx + 1]
        print('Imbalance in ',root)
        print('Problematic tower: ',prob_tower)
        print('Correct weight: ',orig_data[prob_tower][0] - weight_diff)
        exit()
    dd[root][0] = dd[root][0] + sum(weights)
    return dd[root][0]

data = load_input('day7.dat')
orig_data = copy.deepcopy(data)
print('Part 1: ',part1(data))
print('Part 2:')
part2(data,part1(data))