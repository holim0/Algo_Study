#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int T, N;

bool comp(pair<int, int> &a, pair<int, int> &b){

    return a.first< b.first;
}
int main(){

    cin>>T;

    for (int i = 0; i < T; i++)
    {
        cin>>N;
        int result=0;
        vector<pair<int, int>> v;
        vector<int> tmp;
        int s1, s2;
        for (int j = 0; j < N; j++)
        {
            cin>>s1>>s2;
            v.push_back({s1, s2});
        }
        sort(v.begin(), v.end(), comp);

        tmp.push_back(v[0].second);
        
        for (int i = 1; i < v.size(); i++)
        {   
            
            if(v[i].second>tmp.back()) {
                continue;
            }
            else{
                tmp.push_back(v[i].second);
            }
        }
        
        cout<<tmp.size()<<endl;
        
    }
    
    





    return 0;
}