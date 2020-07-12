#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#define MAX 987654321
using namespace std;

int N;
int people[13];
int map[13][13]={0, };
bool check[13]={false, };

vector<int> v;
int minresult=MAX;

bool isConnect(vector<int> &a){

    queue<int> q;
    bool tmpcheck[13]={false, };
    q.push(a[0]);
    tmpcheck[a[0]]=true;

    // for(int i=0; i<a.size(); i++){
    //     cout<<a[i];
    // }
    

    while(!q.empty()){
        //cout<<"큐프론트:"<<q.front()<<endl;
        for(int i=1; i<=N; i++){
            bool ishere=false;
            for(int j=0; j<a.size(); j++){
                if(i==a[j]) {
                    ishere=true; 
                    break;
                }
            }
            
            if(!tmpcheck[i] && map[q.front()][i] && ishere){
                tmpcheck[i]=true;
                //cout<<"inside q:"<<i<<endl;
                q.push(i);
            }
        }
        q.pop();
    }
    
    for(int i=0; i<a.size(); i++){
        if(!tmpcheck[a[i]]) return false;
    }

    return true;

}

int cal(){

    vector<int> n1;
    vector<int> n2;
    int s1=0, s2=0;
    for(int i=1; i<=N; i++){
        if(!check[i]) n2.push_back(i);
        else n1.push_back(i);
    }
    
    // cout<<"첫번째 구역 개수: "<<n1.size()<<endl;
    // cout<<"두번째 구역 개수: "<<n2.size()<<endl;

    if(n1.size()>1){
        if(!isConnect(n1)) return MAX;
        for(int i=0; i<n1.size(); i++){
            s1+=people[n1[i]];
        }
    }else{
        s1=people[n1[0]];
    }
    if(n2.size()>1){
        //cout<<isConnect(n2)<<endl;
        if(!isConnect(n2)) return MAX;
        for(int i=0; i<n2.size(); i++){
            s2+=people[n2[i]];
        }
    }else{
        s2=people[n2[0]];
    }
    

    //cout<<abs(s1-s2)<<endl;
    return abs(s1-s2);



}


void go(int start, int cnt, int base){
    if(cnt==base){
        //cout<<"현재 조합:"<<endl;
        // for(int i=0; i<v.size(); i++){
        //     cout<<v[i]<<" ";
        // }
        // cout<<'\n';
        minresult= min(cal(), minresult);
        //cout<<"minresult:"<<minresult<<endl;
        return;
    }
    
    for (int i =start; i <=N; i++)
    {   
        if(!check[i]){
            check[i]=true;
            v.push_back(i);
            go(i, cnt+1, base);
            check[i]=false;
            v.pop_back();
        }
    }
    
}

int main(){

    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>people[i];
    }
    int n, val;
    for (int i = 1; i <=N ; i++)
    {
       cin>>n;
       for (int j = 0; j < n; j++)
       {
           cin>>val; 
           map[i][val]=1; map[val][i]=1;
       }
    }


    for(int i=1; i<=N/2; i++){
        go(1, 0, i);
    }
    
    
    if(minresult==MAX){
        cout<<-1<<endl;
        return 0;
    }
    
    cout<<minresult<<endl;





    return 0; 
}