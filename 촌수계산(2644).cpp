#include<iostream>

using namespace std;

int n, p1, p2, m;
int map[105][105];
bool check[105]={false, };
int result=0;

void go(int start, int target, int cnt){

    if(start==target){
        result=cnt;
        return;
    }

    for(int i=1; i<=n; i++){
        if(!check[i] && map[start][i]==1){
            check[i]=true;
            go(i, target, cnt+1);
        }

    }


}


int main(){

    cin>>n;
    cin>>p1>>p2;
    cin>>m;
    int val1, val2;
    for (int i = 0; i < m; i++)
    {
        cin>>val1>>val2;
        map[val1][val2]=1;
        map[val2][val1]=1;
    }
    check[p1]=true;
    go(p1, p2, 0);
    

    if(result==0){
        cout<<-1<<endl;
        return 0;
    }

    cout<<result<<endl;

    return 0;
}