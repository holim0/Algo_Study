#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

int N;
long long num[105];
long long oper[105][2];
bool check[105]={false, };
vector<long long> v;

void go(int cur){

    if(v.size()==N){

        for (int i = 0; i < v.size(); i++)
        {
            cout<<v[i]<<" ";
        }
        cout<<endl;
        exit(0);
    }
    

    for (int i = 0; i < N; i++)
    {
        if(!check[i] && num[i]==oper[cur][0]){
            check[i]=true;
            v.push_back(num[i]);
            go(i);
            check[i]=false;
            v.pop_back();
        }

        if(!check[i] && num[i]==oper[cur][1]){
            check[i]=true;
            v.push_back(num[i]);
            go(i);
            check[i]=false;
            v.pop_back();
        }
    }
    


}

int main(){

    cin>>N;

    for (int i = 0; i < N; i++)
    {
        cin>>num[i];
    }

    for (int i = 0; i < N; i++)
    {
        if(num[i]%3==0){
            oper[i][0]=num[i]/3;
        }
        oper[i][1]=2*num[i];
    }

    for (int i = 0; i < N; i++)
    {   
        v.clear();
        memset(check, false, sizeof(check));
        v.push_back(num[i]);
        check[i]=true;
        go(i);
        check[i]=false;
        v.pop_back();
    }
    


    return 0;
}