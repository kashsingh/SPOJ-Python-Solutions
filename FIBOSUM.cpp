// We know the fact that: Sum of first n Fibonacci numbers is the (n+2)th Fibonacci number.
// So (F(N) + F(N + 1) + ... + F(M)= F(M+2) - F(N+1).
// Now all we need is to calculate 2 Fibonacci nos.
// It uses the Matrix exponentiation algorithm to calculate Fibonacci nos.

#include<stdio.h>
using namespace std;
typedef long long ll;
#define MOD 1000000007

void multiply(ll F[2][2], ll M[2][2]);

void power(ll F[2][2], ll n);

/* function that returns nth Fibonacci number */
ll fib(ll n)
{
  ll F[2][2] = {{1,1},{1,0}};
  if (n == 0)
    return 0;
  power(F, n-1);
  return F[0][0];
}

void power(ll F[2][2], ll n)
{
  if( n == 0 || n == 1)
      return;
  ll M[2][2] = {{1,1},{1,0}};

  power(F, n/2);
  multiply(F, F);

  if (n%2 != 0)
     multiply(F, M);
}

void multiply(ll F[2][2], ll M[2][2])
{
  ll x =  (F[0][0]*M[0][0] + F[0][1]*M[1][0])%MOD;
  ll y =  (F[0][0]*M[0][1] + F[0][1]*M[1][1])%MOD;
  ll z =  (F[1][0]*M[0][0] + F[1][1]*M[1][0])%MOD;
  ll w =  (F[1][0]*M[0][1] + F[1][1]*M[1][1])%MOD;

  F[0][0] = x;
  F[0][1] = y;
  F[1][0] = z;
  F[1][1] = w;
}

int main(){
    int t;
    ll n, m,result;
    scanf("%d",&t);
    while(t--){
        scanf("%lld %lld",&n,&m);
        if(n>m){
            printf("Error!!");
        }
        else{
            result=(fib(m+2)-fib(n+1))%MOD;
            if (result<0){
                result+=MOD;
            }
            printf("%lld\n", result);
        }
    }
    return 0;
}
