#include<iostream>

using namespace std; 

int gcd(int a, int b){
	while(b!=0){
		int r = a%b;
		a= b;
		b= r;
	}
	return a;
}

int main(){

    int a, b, c, d;
    cin>>a>>b>>c>>d;

    int low= b * d;
    int top= a*d+b*c;

    int g=gcd(low, top);

    cout<<top/g<<" "<<low/g<<endl;
    return 0;
}