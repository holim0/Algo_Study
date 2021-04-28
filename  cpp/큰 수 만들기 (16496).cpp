#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;
vector<string> v;

bool comp(string a, string b){
    return a+b > b+a;
}

int main(){


    int n;

    cin>>n;

    for (int i = 0; i < n; i++)
    {
        string s;
        cin>>s;
        v.push_back(s);
    }
    
    sort(v.begin(), v.end(), comp);

    string result="";

    for (int i = 0; i < v.size(); i++)
    {
        result+=v[i];
    }
    if(result[0]=='0'){
        cout<<0<<endl;
        return 0;
    }
    cout<<result<<endl;


    return 0;
}