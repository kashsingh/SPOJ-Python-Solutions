"""TLE in this solution also."""
import sys;   

inp = sys.stdin.read().split()    
t = int(inp[0])
readAt = 1
for i in xrange (0,t):
    x,y,z = map(int,inp[readAt:readAt+3])    # Read the next three elements
    n = (2*z)/(x+y)
    d = (y-x)/(n-5)
    a = x-(2*d)
    print n
    print ' '.join([str(a+ti*d) for ti in xrange(n)]) # More compact and faster
    readAt += 3   # Increment the index from which to start the next read