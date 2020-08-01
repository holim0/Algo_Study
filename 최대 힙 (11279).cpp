#include<iostream>
#include<queue>

using namespace std;

priority_queue<int> pq;

int N;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>N;

    for (int i = 0; i < N; i++)
    {   
        int oper;
        cin>>oper;
        if(oper==0){
            if(pq.empty()){
                cout<<0<<'\n';
            }
            else{
                cout<<pq.top()<<'\n';
                pq.pop();
            }    
        
        }else{
            pq.push(oper);
        }
    }
    




    return 0;
}