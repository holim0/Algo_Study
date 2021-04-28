#include<iostream>

using namespace std;
int fibo[25];

int main(){

    int n;
    cin>>n;

    fibo[0]=0;
    fibo[1]=1;
    

    for (int i = 2; i <=n; i++)
    {
        fibo[i]=fibo[i-1]+fibo[i-2];
        
    }
    

    cout<<fibo[n]<<endl;
    


    return 0;
}