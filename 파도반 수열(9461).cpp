#include<iostream>

using namespace std;

int T;
long long num[105]={0, 1, 1, 1, 2, 2,};
int main(){

    cin>>T;

    
    for(int i=6; i<=100; i++){
        num[i]=num[i-1]+num[i-5];
    }

    for (int i = 0; i < T; i++)
    {
        int a;
        cin>>a;
        cout<<num[a]<<endl;
    }
    




    return 0;
}