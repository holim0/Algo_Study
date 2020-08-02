#include<iostream>
#include<string>
#include<vector>
#include<cstring>

#define MAX 9987654321

using namespace std;

int n;
char oper[10];
long long maxr=-1;
long long minr=MAX;
bool check[10]={false, };

void dfs(long long start, int idx, long long num){
    
    if(idx==n){
        maxr= maxr<num ? num : maxr;
        minr= minr>num ? num : minr;
        return;
    }

    if(oper[idx]=='<'){
        for (int i = 0; i <=9; i++)
        {
            if(!check[i] && start<i){
                check[i]=true;
                dfs(i, idx+1, num*10+i);
                check[i]=false;
            }
        }
    }

    if(oper[idx]=='>'){
        for (int i = 0; i <=9; i++)
        {
            if(!check[i] && start>i){
                check[i]=true;
                dfs(i, idx+1, num*10+i);
                check[i]=false;
            }
        }
    }

}


int main(){
    
    cin>>n;

    for (int i = 0; i < n; i++)
    {
        cin>>oper[i];
    }

    for (int i = 0; i <= 9; i++)
    {
        memset(check, false, sizeof(check));
        check[i]=true;
        dfs(i, 0, i);
        check[i]=false;
    }

    string s1=to_string(maxr);
    string s2=to_string(minr);

    if(s1.size()<n+1){
        s1='0'+s1;
    }

    if(s2.size()<n+1){
        s2='0'+s2;
    }

    cout<<s1<<'\n'<<s2<<endl;




    return 0;
}