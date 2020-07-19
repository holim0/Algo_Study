#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

vector<pair<int, pair<int, string>>> v;

int n;

bool comp(pair<int, pair<int, string>> &a, pair<int, pair<int, string>> &b){

    if(a.second.first==b.second.first){
        return a.first<b.first;
    }
    return a.second.first<b.second.first;

}

int main(){

    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);


    cin>>n;
    int age; string name;

    for (int i = 0; i < n; i++)
    {
       cin>>age>>name;
       v.push_back({i, {age, name}});
    }

    sort(v.begin(), v.end(), comp);


    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i].second.first<<" "<<v[i].second.second<<'\n';
    }
    
    



    return 0;
}