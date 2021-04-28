#include<iostream>

using namespace std;  
int num[52][52];
bool check[52][52];
int N, M, T;
int dir[]={1, -1};

void reset(){

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            check[i][j]=false;
        }
        
    }
    
}

void move(int x, int d, int k){
    int cnt=k%M;
    for (int i = 1; i <= N; i++)
    {
        if(i%x==0){
            if(d==0){
                for (int n = 0; n < cnt; n++)
                {
                    int tmp=num[i][M];
                    for (int j = M; j>0; j--)
                    {
                        num[i][j]=num[i][j-1];
                    }
                    num[i][1]=tmp;
                }
            }else{
                for (int n = 0; n < cnt; n++)
                {
                    int tmp=num[i][1];
                    for (int j = 1; j < M; j++)
                    {
                        num[i][j]=num[i][j+1];
                    }
                    num[i][M]=tmp;
                }
            }
        }
    }
    
    // for (int i = 1; i <=N; i++)
    // {
    //     for (int j = 1; j <=M; j++)
    //     {
    //         cout<<num[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }
    // cout<<endl;
    

}

void cal(){

    
    bool del=false;

    reset();

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <=M; j++)
        {
            if(num[i][j]==0) continue;
            if(j==1){
                if(num[i][j]==num[i][M]){
                    del=true;
                    check[i][j]=check[i][M]=true;
                }
                if(num[i][j]==num[i][j+1]){
                    del=true;
                    check[i][j]=check[i][j+1]=true;
                }
            }else if(j==M){
                if(num[i][j]==num[i][1]){
                    del=true;
                    check[i][j]=check[i][1]=true;
                }
                if(num[i][j]==num[i][j-1]){
                    del=true;
                    check[i][j]=check[i][j-1]=true;
                }
            }else{
                if(num[i][j]==num[i][j-1]){
                    del=true;
                    check[i][j]=check[i][j-1]=true;

                }
                if(num[i][j]==num[i][j+1]){
                    del=true;
                    check[i][j]=check[i][j+1]=true;
                }
            }

            if(i>1){
                if(num[i][j]==num[i-1][j]){
                    del=true;
                    check[i][j]=check[i-1][j]=true;
                }
                if(num[i][j]==num[i+1][j]){
                    del=true;
                    check[i][j]=check[i+1][j]=true;
                }
            }else{
                if(num[i][j]==num[i+1][j]){
                    del=true;
                    check[i][j]=check[i+1][j]=true;
                }
            }

        }
        
    }
    if(del){
        for (int i = 1; i <=N; i++)
        {
            for (int j = 1; j <=M; j++)
            {
                if(check[i][j]){
                    num[i][j]=0;
                }
            }
            
        }
        
    }

    else{
        int sum=0;
        int cnt=0;
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= M; j++)
            {
                if(num[i][j]!=0){
                    sum+=num[i][j];
                    cnt++;
                }
            }
            
        }

        double aver=(double)sum/(double)cnt;
        
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= M; j++)
            {
                if((double)num[i][j]<aver &&num[i][j]!=0){
                    num[i][j]+=1;
                }else if((double)num[i][j]>aver && num[i][j]!=0){
                    num[i][j]-=1;
                }
            }
            
        }
    }
    

}
int main(){

    cin>>N>>M>>T;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            cin>>num[i][j];
        }
    }


    
    for (int i = 0; i < T; i++)
    {
        int x, d, k;
        cin>>x>>d>>k;
        move(x, d, k);
        cal();
    }
    

    int result=0;
    
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            result+=num[i][j];
        }
        
    }
    
    cout<<result<<endl;

    return 0;
}