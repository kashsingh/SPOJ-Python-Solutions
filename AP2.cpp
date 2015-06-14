#include <stdio.h>
using namespace std;

int main()
{ int t;
    scanf("%d",&t);
    while(t--){
    long long tt,tlt,sumT,n,d,a,i;
    scanf("%lld%lld%lld",&tt,&tlt,&sumT);
    n=2*sumT/(tt+tlt);
    printf("%lld\n",n);
    d=(tlt-tt)/(n-5);
    a=tt-2*d;
    for(i=0;i<n;i++){
            printf("%lld",(a+i*d));
            printf(" ");
        }

    }
    return 0;
}
