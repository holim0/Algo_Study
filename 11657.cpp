#include<iostream>
#include<utility>
#include<vector>

const int INF = 2e9;

using namespace std;
int N, M;
int dist[501];
bool cycle=false;
vector<pair<int, int>> map[501];

void get(){

    
    dist[1]=0;
    
    for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			for (int k = 0; k < map[j].size(); k++) {
				int cur = map[j][k].first;
				int cost = map[j][k].second;
				if (dist[j] != INF && dist[cur] > cost + dist[j]) {
					dist[cur] = cost + dist[j]; //최소값으로 갱신
					if (i == N) cycle = true;
				}
			}
		}
	}
    
    
    if(cycle) {
        cout<<-1<<endl;
        return;
    }
    else{
        for (int i = 2; i <=N; i++)
        {
            if(dist[i]==INF) cout<<-1<<endl;
            else{
                cout<<dist[i]<<endl;
            }
        }
        
    }
    

}

int main(){

    cin>>N>>M;

    
    for (int i = 0; i < N; i++)
    {
        dist[i]=INF;
    }
    

    for (int i = 0; i < M; i++)
    {
        int a, b, w;
        cin>>a>>b>>w;
        map[a].push_back({b, w});

    }
    
    get();



    return 0;
}