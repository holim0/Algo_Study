#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N, M;

vector<pair<int, pair<int, int>>> v;

int result=0;

bool check[1005]={false, };

bool checkAll(){

    for (int i = 1; i <= N; i++)
    {
        if(!check[i]) return false;
    }
    
    return true;
}

int main(){

    cin>>N>>M;

    int s, e, w;

    for (int i = 0; i < M; i++)
    {
        cin>>s>>e>>w;
        v.push_back({w, {s, e}});
    }

    sort(v.begin(), v.end());
    check[1]=true;
    int n1, n2, cost;
    while(!checkAll()){

        for (int i = 0; i < v.size(); i++)
        {
            n1=v[i].second.first;
            n2=v[i].second.second;
            cost=v[i].first;

            if(check[n1] || check[n2]){
                if(check[n1] && check[n2]) continue;
                else{
                    check[n1]=true;
                    check[n2]=true;
                    result+=cost;
                    break;
                }
            }
        }
        
        
    }
    

    cout<<result<<endl;
    



    return 0;
}