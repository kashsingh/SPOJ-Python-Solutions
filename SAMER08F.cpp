#include<iostream>
using namespace std;
#include<cstdio>
int main()
{
    while(1)
    {
        int no;
        cin>>no;
        if(no==0)
            break;
        int total=0;   
        while(no>0)
        {
            total = total + (no*no);
            no--;
        }
        cout<<total<<"\n";
    }
    return 0;
}