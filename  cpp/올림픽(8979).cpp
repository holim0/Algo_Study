#include<iostream>
#include<vector>
#include<algorithm>


using namespace std;

int N, K;

vector<pair<pair<int, int>, pair<int, int>>> v;

bool comp(pair<pair<int, int>, pair<int, int>> &a, pair<pair<int, int>, pair<int, int>> &b){

    if(a.first.second==b.first.second){
        if(a.second.first==b.second.first) return a.second.second>b.second.second;
        else return a.second.first > b.second.first;
    }
    return a.first.second > b.first.second;
}

int main(){

    cin>>N>>K;
    int a, b, c, d;
    for (int i = 0; i < N; i++)
    {
        cin>>a>>b>>c>>d;
        v.push_back({{a, b}, {c, d}});
    }

    sort(v.begin(), v.end(), comp);
    int order;
    for (int i = 0; i < v.size(); i++)
    {
        if(K==v[i].first.first){
            order=i+1;
            for (int j = 0; j < i; j++)
            {
                if(v[i].first.second==v[j].first.second && 
                v[i].second.first==v[j].second.first && v[i].second.second== v[j].second.second){
                    order=j+1;
                    break;
                }
            }

            cout<<order<<endl;
            break;
            
        }
    }
    

    return 0;
}