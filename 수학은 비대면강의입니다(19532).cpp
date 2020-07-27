#include<iostream>

using namespace std;

int fir[3];
int sec[3];
int a, b, c, d, e, f;
int main(){

    cin>>a>>b>>c>>d>>e>>f;


    
    int y=((c*d)-(f*a))/((b*d)-(a*e));
    int x=((c*e)-(f*b))/((a*e)-(b*d));
    cout<<x<<" "<<y<<endl;




    

    return 0;
}