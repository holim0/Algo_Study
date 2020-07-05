#include<iostream>
#include<algorithm>
#include<string>
#include<vector>


using namespace std;


int main(){


    string s="110";
    vector<char> v;
    for(int i=0; i<s.size(); i++){
        v.push_back(s[i]);
    }

    sort(v.begin(), v.end());
    
    for(int i=0; i<v.size(); i++){
        cout<<v[i]<<endl;
    }

    

    return 0;

}