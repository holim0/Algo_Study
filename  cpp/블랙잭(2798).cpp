#include<iostream>
#include<vector>

using namespace std;

int N, M;
vector<int> t;
int result=-1;
int num[105];
bool check[105]={false, };


void go(int start, int cnt){
    if(cnt==3){
        int sum=0;
        sum+=t[0]+t[1]+t[2];

        if(sum<=M){
            result= sum> result ? sum : result;
        }
        return;
    }

    for (int i = start; i < N; i++)
    {
        if(!check[i]){
            check[i]=true;
            t.push_back(num[i]);
            go(i, cnt+1);
            check[i]=false;
            t.pop_back();
        }
    }
    
    


}
int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        cin>>num[i];
    }

    go(0, 0);
    

    cout<<result<<endl;


    return 0;
}