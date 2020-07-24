#include<iostream>

using namespace std;

int N, K;   

bool check[1005]={false, };



int main(){

    cin>>N>>K;
    int cnt=0;
    for (int i = 2; i <= N; i++)
    {
        if(!check[i]){
            check[i]=true;
            cnt++;
            if(cnt==K){
                cout<<i<<endl;
                return 0;
            }
            for(int j=i+i; j<=N; j+=i){
                if(!check[j]){
                    check[j]=true;
                    cnt++;
                    if(cnt==K){
                        cout<<j<<endl;
                        return 0;

                    }
                }
            }
        }
    }
    


    return 0;
}