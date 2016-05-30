def gcd(a,b):
    if b > a:
        return gcd(b,a)
    r = a%b
    if r == 0:
        return b
    return gcd(r,b)
    
for t in xrange(input()):
    N,a,b=raw_input().split()
    ans=gcd(int(a),int(b))
    print N*ans