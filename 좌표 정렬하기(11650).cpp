#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

vector<pair<int, int>> v;

bool comp(pair<int, int> &a, pair<int, int> &b){
   
    if(a.first==b.first){
        return a.second<b.second;
    }

    return a.first<b.first;

}

int main(){

    int n; cin>>n;
    int x, y;
    for (int i = 0; i < n; i++)
    {
        cin>>x>>y;
        v.push_back({x, y});
    }
    
    sort(v.begin(), v.end(), comp);


    for (int i = 0; i < n; i++)
    {
        cout<<v[i].first<<" "<<v[i].second<<'\n';
    }
    


    return 0;
}