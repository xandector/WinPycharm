# 大马3包，中马2包，小马0.5包
# 100匹马100包，问各有多少马

bigHorse = 3
midHorse = 2
tinyHorse = 0.5
bags = 100
horses = 100

for bi in range(0, bags // bigHorse + 1):
    for mi in range(0, bags // midHorse + 1):
        for ti in range(0, int(bags // tinyHorse + 1)):
            if (bi * bigHorse + mi * midHorse + ti * tinyHorse == bags) and (bi + mi + ti == horses):
                print('There are', bi, 'Big Horses,', mi, 'Midium Horses and', ti, 'Tiny Horses.')
