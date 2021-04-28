#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N;

vector<pair<long long, long long>> v;
int result=1;




bool comp(pair<long long, long long> &a, pair<long long, long long> &b){
    
    if(a.second==b.second){
        return a.first<b.first;
    }
    
    return a.second<b.second;
}
int main(){

    cin>>N;

    for (int i = 0; i < N; i++)
    {
        long long a, b;
        cin>>a>>b;
        v.push_back({a, b});
    }

    sort(v.begin(), v.end(), comp);

    int end=v[0].second;

    for (int i = 1; i < v.size(); i++)
    {
        if(end>v[i].first) continue;
        else{
            end=v[i].second;
            result++;
        }
    }
    

    cout<<result<<endl;
    return 0;

}