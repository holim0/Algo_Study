#include<iostream>
#define MIN 987654321
#include<queue>

using namespace std;

bool check[1000005]={false, };
int  F, S, G, U, D;
int result=MIN;
queue<pair<int, int>> q;

int main(){

    cin>>F>>S>>G>>U>>D;
    

    
    check[S]=true;
    q.push({S, 0});
    while(!q.empty()){
        int cur=q.front().first; int cnt=q.front().second;
        q.pop();
        if(cur==G){
            result=cnt;
            break;
        }

        if(!check[cur+U] && cur+U<=F){
            check[cur+U]=true;
            q.push({cur+U, cnt+1});
        }

        if(!check[cur-D] && cur-D>=1){
            check[cur-D]=true;
            q.push({cur-D, cnt+1});
        }

    }
    

    

    if(result==MIN){
        cout<<"use the stairs"<<endl;
        return 0;
    }

    cout<<result<<endl;



    return 0;
}