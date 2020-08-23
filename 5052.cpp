#include<iostream>
#include<algorithm>
#include<string>
#define MAX 10000+5

using namespace std;
int t, n;

string num[MAX];

void sol(){

    for (int i = 0; i < n; i++)
    {
        string cur=num[i];
        string val="";
        for (int j = 0; j < cur.size(); j++)
        {
            val+=num[i+1][j];
        }
        if(cur==val){
            cout<<"NO"<<endl;
            return;
        }
        
    }

    cout<<"YES"<<endl;
    

}

int main(){

    cin>>t;

    for (int i = 0; i < t; i++)
    {
        cin>>n;
        for (int j = 0; j < n; j++)
        {
            cin>>num[j];            
        }

        sort(num, num+n);
        sol();
    }
    


    return 0;
}