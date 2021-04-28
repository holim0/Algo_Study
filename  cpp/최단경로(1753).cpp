#include<iostream>
#define INF 987654321
#include<algorithm>
#include<queue>
#include<cstring>
#include<vector>

using namespace std;

vector<pair<int, int>> tmp[20005];
int dist[20005];

int main(){

    
    int V, E, K, u, v, w;

    cin>>V>>E>>K;

    for (int i = 0; i < E; i++)
    {
        cin>>u>>v>>w;
        tmp[u].push_back({w, v});
        
    }
    for (int i = 1; i <=V; i++)
    {
        dist[i]=INF;
    }
    

    dist[K]=0;

    priority_queue<pair<int, int>> q;

    q.push({0, K});

    while(!q.empty()){
        int cur=q.top().second;
        int curdist=-q.top().first;
        q.pop();

        if(dist[cur]<curdist) continue;

        for (int i = 0; i < tmp[cur].size(); i++)
        {
            int next=tmp[cur][i].second;
            int nextdist=curdist+tmp[cur][i].first;

            if(nextdist<dist[next]){
                dist[next]=nextdist;
                q.push({-nextdist, next});
            }

            
        }
        
    }


    for (int i = 1; i <=V; i++)
    {
        if(dist[i]==INF){
            cout<<"INF"<<'\n';
        }else{
            cout<<dist[i]<<'\n';
        }
        
    }
    

    return 0;
}