#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

bool comp(string a, string b){

    if (a.size()==b.size()){
        return a<b;
    }

    return a.size()<b.size();

}

int main(){

    vector<string> v;

    int n;
    string s;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        cin>>s;
        v.push_back(s);
    }
    

    sort(v.begin(), v.end(), comp);
    
    for (int i = 0; i < v.size(); i++)
    {
        if(i>0 && v[i]==v[i-1]) continue;
        cout<<v[i]<<endl;
    }
    
    return 0;
}