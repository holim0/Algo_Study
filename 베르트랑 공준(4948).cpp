#include<iostream>
#define MAX 123456*2
using namespace std;

bool check[MAX]={false, };
void getSosu(){


    check[0]=true;
    check[1]=true;

    for (int i = 2; i*i <=MAX; i++)
    {
        for (int j = i+i; j <=MAX; j+=i)
        {
            if(!check[j]) check[j]=true;
        }
        
    }

}

int sol(int n){

    int cnt=0;

    for (int i = n+1; i <= 2*n; i++)
    {
        if(!check[i]) cnt++;
    }
    
    return cnt;
    
}


int main(){

    int n;

    getSosu();

    while(1){
        cin>>n;
        if(n==0) break;
        cout<<sol(n)<<endl;

    }
    
    





    return 0;
}
