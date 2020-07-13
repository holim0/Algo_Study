#include<iostream>

using namespace std;

int firstMap[53][53];
int updateMap[53][53];
int copyMap[53][53];


int R, C, T;

int dx[]={-1, 1, 0, 0};
int dy[]={0,  0, -1, 1};

int getResult(){

    int sum=0;

    for (int i = 1; i<=R; i++)
    {
        for (int j = 1; j <=C; j++)
        {
            if(updateMap[i][j]>0) sum+=updateMap[i][j];
        }
    }
    return sum;

}

void Copy(){


    for (int i = 1; i<=R; i++)
    {
        for (int j = 1; j <=C; j++)
        {
            updateMap[i][j]=firstMap[i][j];
        } 
    }
    
}

void updateM(){

    for (int i = 1; i<=R; i++)
    {
        for (int j = 1; j <=C; j++)
        {
            updateMap[i][j]=copyMap[i][j];
        } 
    }

}

void dust(){
    int cnt, goval;
    for (int i = 1; i<=R; i++)
    {
        for (int j = 1; j <=C; j++)
        {
            if(updateMap[i][j]!=0 && updateMap[j][j]!=-1){
                goval=updateMap[i][j]/5;
                cnt=0;
                for(int k=0; k<4; k++){
                    int nx=i+dx[k]; int ny=j+dy[k];
                    if(updateMap[nx][ny]!=-1 && nx>=1 && nx<=R && ny>=1 && ny<=C){
                        cnt++;
                        copyMap[nx][ny]+=goval;
                    }
                }
                copyMap[i][j]-=(cnt*goval);
            }
        } 
    }
}

void clean(){

    int firstx, firsty, secx, secy;
    int tmpmap[52][52];

    

    for (int i = 1; i<=R; i++)  // 배열 돌리기 위해서 쓰는 기준 맵
    {
        for (int j = 1; j <=C; j++)
        {
            tmpmap[i][j]=copyMap[i][j];
        } 
    }

    
        for (int i = 1; i<=R; i++)
        {
            
            if(copyMap[i][1]==-1){
                firstx=i; firsty=1;
                secx=i+1, secy=1;
                break;
            }    
        }
        
        
        //첫번째 구역 순환//
        int val1=tmpmap[firstx][C];
        for(int i=C; i>=3; i--){         //아래쪽
            copyMap[firstx][i]=copyMap[firstx][i-1];
        }
        copyMap[firstx][2]=0;


        int val2=tmpmap[1][C];
        for (int i = 1; i <firstx; i++)  //오른쪽
        {
            if(i==firstx-1){
                copyMap[i][C]=val1;
            }
            else{
                copyMap[i][C]=copyMap[i+1][C];
            }
        }

        int val3=tmpmap[1][1];
        for (int i = 1; i < C; i++)    //위쪽
        {
            if(i==C-1){
                copyMap[1][i]=val2;
            }else{
                copyMap[1][i]=copyMap[1][i+1];
            }
        }
        
        for(int i=firstx-1; i>1; i--){  //왼쪽
            if(i==2){
                copyMap[i][1]=val3;
            }else{
                copyMap[i][1]=copyMap[i-1][1];
            }
        }
     ////////////////////////////////////////////////////////// 두번째///


    int val4=tmpmap[secx][C];
    for(int i=C; i>2; i--){     // 맨위
        copyMap[secx][i]=copyMap[secx][i-1];
    }
    copyMap[secx][2]=0;

    int val5=tmpmap[R][C]; 
    for(int i=R; i>secx ;i--){  // 오른쪽
        
        if(i==secx+1){
            copyMap[i][C]=val4;
        }else{
            copyMap[i][C]= copyMap[i-1][C];
        }
        
    }


    int val6=copyMap[R][1];
    for (int i = 1; i < C; i++)    //아래쪽
    {
        if(i==C-1){
            copyMap[R][i]=val5;
        }else{
            copyMap[R][i]=copyMap[R][i+1];
        }
    }
    

    for (int i = secx+1; i < R; i++)  //왼쪽
    {
        if(i==R-1){
            copyMap[i][1]=val6;
        }else{
            copyMap[i][1]=copyMap[i+1][1];
        }
    }

}




int main(){

    cin>>R>>C>>T;

    for (int i = 1; i <= R; i++)
    {
        for (int j = 1; j <=C; j++)
        {
            cin>>firstMap[i][j];
            copyMap[i][j]=firstMap[i][j];
        }
        
    }
    
    Copy();  //초기화
    for(int i=0; i<T; i++){
        dust();
        clean();
        updateM();
    }

    cout<<getResult()<<endl;

    return 0;
}