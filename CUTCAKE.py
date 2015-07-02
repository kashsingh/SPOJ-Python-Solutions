# For every n cut we will have n^2+n+2 pieces so a binary search for the solution of quadratic equation will do the job.
def binary(n):
    low,mid=0,0
    high=10000000;
    while(low<high):
        mid=(low+high)/2
        k=mid*mid+mid+2
    
        if(k>=n):
            high=mid
        else:
            low=mid+1;
    return low


def main():
    for _ in xrange(input()):
        ans=binary(2*input())
        print ans

main()
        