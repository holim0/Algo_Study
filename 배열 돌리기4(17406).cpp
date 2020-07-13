#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#define MAX 987654321

using namespace std;

int arr[52][52];
int copyarr[52][52]={0, };
int orginarr[52][52];
int N, M, opercnt;

int progress[8][4];

int minval=MAX;

void cal(int lupx, int lupy, int rdowx, int rdowy){

    
    if(lupx==rdowx && lupy==rdowy){
        return;
    }

    int val= copyarr[lupx][rdowy];
    for (int j = rdowy; j>lupy; j--) // 맨위
    {   
        copyarr[lupx][j]=copyarr[lupx][j-1];
    }

    
        
    int val2=copyarr[rdowx][rdowy];
    for(int j=rdowx; j>lupx; j--) { // 오른쪽
        if (j==lupx+1){
            copyarr[j][rdowy]=val;
        } else{
            copyarr[j][rdowy]=copyarr[j-1][rdowy];
        }
    }

    int val3=copyarr[rdowx][lupy];
    for (int j = lupy; j < rdowy; j++)  // 맨 아래
    {
        if(j==rdowy-1){
            copyarr[rdowx][j]=val2;
        }else{
            copyarr[rdowx][j]=copyarr[rdowx][j+1];
        }
    }

    for (int i =lupx; i < rdowx; i++)  // 왼쪽
    {
        
        if(i==rdowx-1){
            copyarr[i][lupy]= val3;
        }else{
            copyarr[i][lupy]= copyarr[i+1][lupy];
        }
    }
    
    
    cal(lupx+1 ,lupy+1, rdowx-1, rdowy-1);

}

void copymap(){


    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            copyarr[i][j]=arr[i][j];
        }
        
    }
    
}
void backOrigin(){

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            arr[i][j]=orginarr[i][j];
        }
        
    }

}

int getMin(){

    int sum; int minval2=MAX;
    for (int i = 1; i <= N; i++)
    {
        sum=0;
        for (int j = 1; j <= M; j++)
        {
            sum+=copyarr[i][j];
        }
        minval2= minval2>sum ? sum : minval2;
        
    }
    
    return minval2;
    
}


int main(){
    int r, c, s;
    cin>>N>>M>>opercnt;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <=M; j++)
        {
            cin>>arr[i][j];
            orginarr[i][j]=arr[i][j];
        } 
    }

    for (int i = 1; i <= opercnt; i++)
    {
        cin>>r>>c>>s;
        progress[i][1]=r;
        progress[i][2]=c;
        progress[i][3]=s; 
    }
    
    vector<int> operjohab;
    for(int i=1; i<=opercnt; i++){
        operjohab.push_back(i);
    }

    int x1, y1, x2, y2;
    do{
            copymap();
            for(int j=0; j<operjohab.size(); j++){
                int i=operjohab[j];
                //cout<<i<<endl;
                x1=progress[i][1]-progress[i][3];
                y1=progress[i][2]-progress[i][3];
                x2=progress[i][1]+progress[i][3];
                y2=progress[i][2]+progress[i][3];
                
                cal(x1, y1, x2, y2); 
                
            }
            
            minval= minval > getMin() ? getMin() : minval;
        
    }while(next_permutation(operjohab.begin(), operjohab.end()));

    
    

   

    cout<<minval<<endl;
    

    


    return 0;
}