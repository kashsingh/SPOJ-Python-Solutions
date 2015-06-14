#include <iostream>
#include <cmath>
using namespace std;

int main(){
	long long t,a,temp,b,x,y;
	cin >> t;
	while(t--){
		cin >> a >> b >> x >> y;
		if (a>b){		//make a smaller
			temp=a;
			a=b;
			b=temp;
		}
		if(x>y){		//make x smaller
			temp=x;
			x=y;
			y=temp;
		}
		if(a>x && b>y){
			cout << "Escape is possible.\n";
			continue;
		}
		double d_a=(double)a,d_b=(double)b,d_x=(double)x,d_y=(double)y;
		double temp;
		temp = (2.0*d_x*d_y*d_b + (d_y*d_y - d_x*d_x)*(sqrt(d_x*d_x + d_y*d_y - d_b*d_b )));
		cout<<temp;
		temp = temp / (d_x*d_x + d_y*d_y);
		if((a-temp)>0.0000001)
			cout << "Escape is possible.\n";
		else
			cout << "Box cannot be dropped.\n";
	}
}
