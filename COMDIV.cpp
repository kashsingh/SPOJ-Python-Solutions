#include<stdio.h>
#include<math.h>

long long E_GCD(long long m, long long n)
{
   long long  r;

   while (n != 0) {
      r = m % n;
      m = n;
      n = r;
   }
   return m;
}

int main(){
    long long A,B,t;
    scanf("%lld",&t);
    while(t--){
        scanf("%lld %lld",&A,&B);
        long long N = E_GCD(A,B);
        long long ans = 0;
        long long sqt = (int)sqrt(N);
        for(int i = 1 ; i <= sqt; i++){
            if(N % i == 0){
              ans += 2 ;
              if(i == N/i) ans--;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
