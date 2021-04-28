#include<iostream>

using namespace std;



int main(){

    unsigned long long base=1;

    unsigned long long n;
    cin>>n; 
    unsigned long long len=1;
    while(!cin.eof()){
        
        if(base%n==0){
            cout<<len<<endl;
            len=1;
            base=1;
            cin>>n;
        }else
        {
            base=(base*10)%n+1;
            len++;
        }
    
    }



    return 0;
}