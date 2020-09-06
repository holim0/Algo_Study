#include<iostream>

using namespace std;

int main(){

    int a, b, c;

    cin>>a>>b>>c;

    int div= c-b;

    if(div<=0){
        cout<<-1<<endl;

    }else{
        cout<<a/div+1<<endl;
    }


    return 0;
}