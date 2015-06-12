#include <iostream>
#include<stdio.h>
#define ll long long
using namespace std;

/*
  Function to calculate modulus of x raised to the power y
 */
ll modular_pow(ll base, ll exponent, int modulus)
{
    ll result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

int main(){
    ll n,k;
    scanf("%lld %lld ",&n,&k);
    while(n){
        ll a,b,c,d,zsum;
        a=2* modular_pow(n-1,k,10000007);
        b=modular_pow(n,k,10000007);
        c=2*modular_pow(n-1,n-1,10000007);
        d= modular_pow(n,n,10000007);
        zsum=(a+b+c+d)%10000007;
        printf("%lld\n",zsum);
        scanf("%lld %lld ",&n,&k);
    }
return 0;
}
