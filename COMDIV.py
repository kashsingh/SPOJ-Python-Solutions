"""I wrote the code then realised that the time limit is too low to be implemented in Python
   i.e. why no AC in Python for anyone till yet. Now i need to create a C++ version of it."""
   
def E_GCD(A,B):
    i=1
    while(i<=A and i<=B):
        if( A%i==0 and B%i == 0):
            gcd=i;
        i+=1
    return gcd;


def main():
    t= input()
    for case in range(t):
        A,B=map(int,raw_input().split())
        N = E_GCD(A,B)
        print "GCD is: "+str(N)
        ans = 0
        sqt = int(N**0.5)
        i = 1
        while( i <= sqt ):
            if(N % i == 0):
              ans += 2 
              if(i == N/i): ans-=1
            i+=1
        print ans
        
if __name__=="__main__":
    main()
    

