"""**Note: This implementation of EDIST is too slow for SPOJ, it will give TLE as Python gets tricky sometimes to evaluate this.
            Lists are usually cumbersome to operate on large data.

A two-dimensional matrix, m[0..|s1|,0..|s2|] is used to hold the edit distance values:
m[i,j] = d(s1[1..i], s2[1..j])

m[0,0] = 0
m[i,0] = i,  i=1..|s1|
m[0,j] = j,  j=1..|s2|

m[i,j] = min(m[i-1,j-1]
             + if s1[i]=s2[j] then 0 else 1 fi,
             m[i-1, j] + 1,
             m[i, j-1] + 1 ),  i=1..|s1|, j=1..|s2|
m[,] can be computed row by row. Row m[i,] depends only on row m[i-1,]. 
The time complexity of this algorithm is O(|s1|*|s2|). If s1 and s2 have a `similar' length, about `n' say, 
this complexity is O(n2), much better than exponential!"""


def edist(X,Y):
    lenX=len(X)
    lenY=len(Y)
    mat = [[0] * (lenY + 1) for x in xrange(lenX + 1)]
    for x in xrange(lenX + 1):
        mat[x][0] = x
    for x in xrange(lenY + 1):
        mat[0][x] = x
    for x in xrange(1, lenX + 1):
        for y in xrange(1, lenY + 1):
            mat[x][y] = min(
                mat[x - 1][y - 1] + (X[x - 1] != Y[y - 1]),
                mat[x - 1][y] + 1,
                mat[x][y - 1] + 1)
    return mat[-1][-1]
    

def main():
    no=int(raw_input())
    for i in range(no):
        word1=raw_input()
        word2=raw_input()
        print edist(word1,word2)
        
        
if __name__=="__main__":
    main()
    