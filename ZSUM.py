def zsum(n,k):
    '''For a given values of n and k, zsum is given by the formulae: [n^k+n^n+2*(n-1)^k+2*(n-1)^)]%10000007'''
    '''**Note: Python solution is not possible as it not fast enough to compute it. Same algo in C++ will give AC but in Python TLE.'''
    a=2*pow(n-1,k,10000007)
    b=pow(n,k,10000007)
    c=2*pow(n-1,n-1,10000007)
    d=pow(n,n,10000007)
    zsum=(a+b+c+d)%10000007
    print zsum
    
def main():
    while True:
        n,k=map(int,raw_input().split())
        if n==k==0:
            break
        else:
            zsum(n,k)
main()