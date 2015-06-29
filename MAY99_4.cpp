#include<stdio.h>
using namespace std;
#include<vector>


/*
    C(n,r) mod m
    Using recurrence:
    C(i,k) = C(i-1,k-1) + C(i-1,k)

*/

long long C(int n, int r, int MOD)
{
    vector< vector<long long> > C(n+1,vector<long long> (r+1,0));

    for (int i=0; i<=n; i++)
    {
        for (int k=0; k<=r && k<=i; k++)
            if (k==0 || k==i)
                C[i][k] = 1;
            else
                C[i][k] = (C[i-1][k-1] + C[i-1][k])%MOD;
    }
    return C[n][r];
}

int main(){
    int p=10000007;
    int n,r,ans;
    scanf("%d %d",&n,&r);
    n=n-r;
    if(n<0)
        printf("-1\n");

    else if(n==0)
        printf("1\n");
    else
	{
        n=n+r-1;
        r=r-1;
        ans=C(n,r,p);
        printf("%d\n",ans);
    }


    return 0;
}
