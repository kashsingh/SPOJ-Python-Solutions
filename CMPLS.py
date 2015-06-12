def buildCache(seq, c,s):
    cache = [[0 for j in range(s+c)] for i in range(s+2)]
    for i in range(s):
        cache[0][i] = seq[i]
 
    #build
    for order in range(1, s):
        for idx in range(s-order):
            cache[order][idx] = cache[order-1][idx+1]-cache[order-1][idx]
     
    for idx in range(1,1+c):
        cache[s-1][idx] = cache[s-1][0]
         
    #add next sequences to all levels
    for order in range(s-2,-1,-1):
        for idx in range(s-order, s-order+c):
            cache[order][idx] = cache[order][idx-1]+cache[order+1][idx-1]
    
    for e in cache[0][s:s+c+1]:
        print e ,
    print ''        
def solve():
    t = input()
     
    for i in range(t):
        s,c = list(map(int, raw_input().split()))
        seq = list(map(int, raw_input().split()))
        buildCache(seq, c,s)
        
        
             
        
 #1 1 1 1 1 1 1 1 1 2        
solve()