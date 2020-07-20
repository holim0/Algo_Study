#include<iostream>
#include<vector>
#define MAX 987654321

using namespace std;

int N;
int result=MAX;

int map[25][25];
bool check[25]={false,};

vector<int> tmp;

int getsub(vector<int> &a){

    int sum=0, sum2=0;
    bool tmpCheck[25]={false, };
    for (int i = 0; i < a.size(); i++)
    {
        tmpCheck[a[i]]=true;
    }

    for (int i = 1; i <=N; i++)
    {
        if(tmpCheck[i]){
            for (int j = 1; j <=N; j++){
                    if(tmpCheck[j]){
                        sum+=map[i][j];
                }
            }
            
        }else{
            for (int j = 1; j <=N; j++)
            {
                if(!tmpCheck[j]){
                    sum2+=map[i][j];
                }
            }
        }
    }
    
    

    return abs(sum-sum2);
}

void go(int start, int cnt){

    if(cnt==N/2){

        int val=getsub(tmp);
        result= result > val ? val : result;

    }

    for (int i = start; i <=N; i++)
    {
        if(!check[i]){
            check[i]=true;
            tmp.push_back(i);
            go(i, cnt+1);
            check[i]=false;
            tmp.pop_back();
        }
    }
    


}


int main(){

    cin>>N;

    for (int i = 1; i <=N; i++){
        for (int j = 1; j <= N; j++)
        {
            cin>>map[i][j];
        }
    }
    
    go(1, 0);

    cout<<result<<endl;

    return 0;
}