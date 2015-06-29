from fractions import gcd

for i in xrange(input()):
    A,B=map(int,raw_input().split())
    GCD=gcd(A,B)
    print str(B/GCD)+" "+str(A/GCD)