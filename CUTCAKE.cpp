// For every n cut we will have n^2+n+2 pieces so a binary search for the solution of quadratic equation will do the job.
#include<iostream>
typedef long long ll;
typedef long l;
using namespace std;

ll b(ll n)
{
     ll low=0,mid=0;
     ll high=10000000;
     while(low<high)
     {
        ll mid=(low+high)/2;
        ll k=1LL*mid*mid+1LL*mid+1LL*2;

        if(k>=n)
        {
                high=mid;
        }
        else
        {
            low=mid+1;
        }
}

    return low;
}

int main()
{
     int t;
     cin>>t;
     while(t--){
       ll n;
       cin>>n;
       ll ans=b(2*n);
       cout<<ans<<endl;
     }
    return 0;
}
