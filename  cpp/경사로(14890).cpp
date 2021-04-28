#include<iostream>
#include<cmath>

using namespace std;

int N, L;
int map[105][105];
bool check[105][105]={false, };
int result=0;
int num[11];

void reset(){
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            check[i][j]=false;
        }
        
    }
    
}
void garo(){
    bool flag;
    for (int i = 0; i < N; i++)
    {   
        flag=false;
        for (int j = 0; j < N-1; j++)
        {   
            if(abs(map[i][j]-map[i][j+1])>1){
                flag=true;
                break;
            }
            if(map[i][j]> map[i][j+1]){
                if(check[i][j+1]){
                    flag=true; break;
                }
                check[i][j+1]=true;
                for (int k = 1; k < L; k++)
                {
                    if(j+1+k<N && !check[i][j+1+k] && map[i][j+1]==map[i][j+1+k]){
                        check[i][j+1+k]=true;
                    }else{
                        flag=true;
                        break;
                    }
                }
            }else if(map[i][j] < map[i][j+1]){
                if(check[i][j]){
                    flag=true;
                    break;
                }
                check[i][j]=true;
                for(int k=1; k<L; k++){
                    if(j-k>=0 && map[i][j-k]==map[i][j] && !check[i][j-k]){
                        check[i][j-k]=true;
                    }else{
                        flag=true;
                        break;
                    }
                }
                
            }
            if(flag) break;            
        }
        
        if(!flag){
            result++;
        } 
        
    }
    

}

void sero(){

    bool flag;
    for (int i = 0; i < N; i++)
    {   
        flag=false;
        for (int j = 0; j < N-1; j++)
        {   
            if(abs(map[j][i]-map[j+1][i])>1){
                flag=true;
                break;
            }
            if(map[j][i] > map[j+1][i]){
                if(check[j+1][i]){
                    flag=true;
                    break;
                }
                check[j+1][i]=true;
                for (int k = 1; k < L; k++)
                {
                    if(j+1+k<N && !check[j+1+k][i] && map[j+1][i]==map[j+1+k][i]){
                        check[j+1+k][i]=true;
                    }else{
                        flag=true;
                        break;
                    }
                }
            }else if(map[j][i] < map[j+1][i]){
                if(check[j][i]){
                    flag=true;
                    break;
                }
                check[j][i]=true;
                for(int k=1; k<L; k++){
                    if(j-k>=0 && map[j-k][i]==map[j][i] && !check[j-k][i]){
                        check[j-k][i]=true;
                    }else{
                        flag=true;
                        break;
                    }
                }
                
            }
            if(flag) break;            
        }
        
        if(!flag){
            result++;
        } 
        
    }



}

int main(){

    cin>>N>>L;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin>>map[i][j];
        }
    }

    garo();
    
    reset();
    sero();
    cout<<result<<endl;


    return 0;
}