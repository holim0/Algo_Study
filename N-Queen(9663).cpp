#include<iostream>
#include<cstring>

using namespace std;

int map[17][17];
bool check[17][17]={false, };
int N;
int result=0;

bool isOk(int x, int y){

    for(int i=x; i>=0; i--){   //세로
        if(check[i][y]) return false;
    }
    int val1=x; int val2=y;
    while(1){     // 왼 위.
        if(check[val1][val2]) return false;
        val1-=1; val2-=1;
        if(val1<0 || val2<0) break;
    }
    val1=x; val2=y;
    while(1){     // 오른 위.
        if(check[val1][val2]) return false;
        val1-=1; val2+=1;
        if(val1<0 || val2>=N) break;
    }

    return true;

}

void go(int x){

    if(x==N){
        result++;
        return;
    }

    for (int j = 0; j < N; j++)
    {
        if(isOk(x, j) && !check[x][j]){
            check[x][j]=true;
            go(x+1);
            check[x][j]=false;
        }
    }
}


int main(){

    cin>>N;


    go(0);

    
    

    cout<<result<<endl;

    return 0;
}