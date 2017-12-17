genA_test_init = 65
genA_init = 703
genA_factor = 16807

genB_test_init = 8921
genB_init = 516
genB_factor = 48271

genAB_module = 2147483647

def gen(inval, factor, mod):
    return inval*factor % mod

def part1(gai, gaf, gbi, gbf, gabm):
    counter = 0
    for loop in range(40000000):
        gai = gai*gaf % gabm 
        gbi = gbi*gbf % gabm 
        if(bin(gai)[-16:] == bin(gbi)[-16:]):
            counter = counter + 1
    return counter

def part2(gai, gaf, gbi, gbf, gabm):
    counter = 0
    for loop in range(5000000):
        gai = gai*gaf % gabm 
        while(gai % 4 != 0):
            gai = gai*gaf % gabm 

        gbi = gbi*gbf % gabm 
        while(gbi % 8 != 0):
            gbi = gbi*gbf % gabm 

        if(bin(gai)[-16:] == bin(gbi)[-16:]):
            counter = counter + 1
    return counter

#print('Part 1: ', part1(genA_init, genA_factor, genB_init, genB_factor, genAB_module))
print('Part 2: ', part2(genA_init, genA_factor, genB_init, genB_factor, genAB_module))