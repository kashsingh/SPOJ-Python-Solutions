"""Not possible using Python time limit too short for it."""
t=input()
for i in xrange(t):
    tt,tlt,sumT=map(int,raw_input().split())
    n=2*sumT/(tt+tlt)
    print n
    d=(tlt-tt)/(n-5)
    a=tt-2*d
    j=0
    for j in xrange(n-1):
        print a,
        a+=d
    print a
    