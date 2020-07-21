#include<iostream>
#include<string>
using namespace std;


int main(){
    string s;
    string base="CAMBRIDGE";
    cin>>s;
    for (int i = 0; i < base.size(); i++)
    {
        for (int j = 0; j< s.size(); j++)
        {
            if(base[i]==s[j]){
                s[j]='0';
            }
        }
        
    }



    for (int i = 0; i < s.size(); i++)
    {
        if(s[i]!='0') cout<<s[i];
    }
    


    return 0;
}