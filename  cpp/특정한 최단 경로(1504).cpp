#include<iostream>
#include<vector>
#include<queue>
#include<climits>
#include<algorithm>
#define INF 200000000+5
#define MAX 800+5
using namespace std;

int N, E;
long long dist[MAX];
vector<pair<long long, int>> v[MAX];

long long go(int start , int end){

    priority_queue<pair<long long, int>> pq;
    for (int i = 0; i < MAX; i++)
    {
        dist[i]=INF;
    }
    dist[start]=0;
    pq.push({0, start});

    while(!pq.empty()){
        int cur=pq.top().second;
        long long curDist= -pq.top().first; 
        pq.pop();
        if(curDist> dist[cur]) continue;
        for (int i = 0; i < v[cur].size(); i++)
        {
            int next=v[cur][i].second;
            long long nextDist= v[cur][i].first+curDist;

            if(nextDist<dist[next]){
                dist[next]=nextDist;
                pq.push({-nextDist, next});
            }
        }
        

    }

    return dist[end];
    

}
int main(){

    cin>>N>>E;

    for (int i = 0; i < E; i++)
    {
        int a,b, c;
        cin>>a>>b>>c;   
        v[a].push_back({c, b});
        v[b].push_back({c, a});
    }
    int v1, v2;
    cin>>v1>>v2;

    long long n1=go(1, v1);
    long long n2=go(v1, v2);
    long long n3=go(v2, N);

    long long n4=go(1, v2);
    long long n5=go(v2, v1);
    long long n6=go(v1, N);
    long long result1=n1+n2+n3;
    long long result2=n4+n5+n6;


    if(result1>result2){
        if(result2>=INF){
            cout<<-1<<endl;
        }else{
            cout<<result2<<endl;
        }
    }else{
        if(result2>=INF){
            cout<<-1<<endl;
        }else{
            cout<<result1<<endl;
        }
    }
    
    
    

    return 0;
}