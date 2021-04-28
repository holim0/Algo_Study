#include<iostream>
#include<vector>
#include<queue>

using namespace std;
int num[1005];
int N, K;

queue<int> q;
vector<int> result;
int main(){

    cin>>N>>K;


    for (int i = 1; i <= N; i++)
    {
        q.push(i);
    }

    int cnt=0; 
    while(!q.empty()){
        
        
        cnt++;
        if(cnt==K){
            result.push_back(q.front());
            q.pop();
            cnt=0;
        }else{
            q.push(q.front()); 
            q.pop();
        }
        
    }
    
    

    cout<<"<";
    for (int i = 0; i < result.size(); i++)
    {
        if(i==result.size()-1){
            cout<<result[i];
        }else{
            cout<<result[i]<<", ";
        }
        

    }
    cout<<">"<<endl;
    

    return 0;
}