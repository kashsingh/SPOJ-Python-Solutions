from math import pi

const= 1 / (2*pi)
while True:
    L = input()
    if L == 0: break
    print '%.2f' %(L*L*const)