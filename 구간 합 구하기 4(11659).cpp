#include<iostream>


using namespace std; 

int N, M;

int num[100005];


int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin>>N>>M;

    for(int i=1; i<=N; i++){
        cin>>num[i];
        if(i>1){
            num[i]+=num[i-1];
        }
        
    }

    int x, y;
    
    for (int i = 0; i < M; i++)
    {
        cin>>x>>y;
        if(x-1<=0){
            cout<<num[y]<<'\n';
        }else{
            cout<<num[y]-num[x-1]<<'\n';
        }
        
    }
    

    return 0;
}




