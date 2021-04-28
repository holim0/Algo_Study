#include<iostream>

using namespace std;
int map[18][18];
 int n;

int method=0;
void go(int x1, int y1, int x2, int y2){

    if(x2==n && y2==n){
        method++;
        return;
    }

    if(x1==x2){     //가로 포지션
        if(!map[x2][y2+1] && y2+1<=n){  //가로 이동
            go(x1, y1+1, x2, y2+1);
        }

        if(!map[x2+1][y2+1] && !map[x2][y2+1] && !map[x2+1][y2]&& x2+1<=n && y2+1<=n){   // 대각선 아래 이동
            go(x1, y1+1, x2+1, y2+1);
        }

    }else if(y1==y2){    //세로 포지션
        if(!map[x2+1][y2] && x2+1<=n){  // 세로 아래 이동
            go(x1+1, y1, x2+1, y2);
        }

        if(!map[x2][y2+1] &&!map[x2+1][y2+1] &&!map[x2+1][y2] && x2+1<=n && y2+1<=n){  // 대각선 아래 이동
            go(x1+1, y1, x2+1, y2+1);
        }

    }else if(y1+1==y2 && x1+1==x2){   //대각선 포지션

        if(!map[x2][y2+1] && y2+1<=n){ // 가로 이동
            go(x1+1, y1+1, x2, y2+1);
        }
        if(!map[x2+1][y2] && x2+1<=n){   //세로 이동
            go(x1+1, y1+1, x2+1, y2);
        }
        if(!map[x2+1][y2+1] && !map[x2+1][y2] && !map[x2][y2+1] && x2+1<=n && y2+1<=n){ // 대각선 이동
            go(x1+1, y1+1, x2+1, y2+1);
        }   


    }



}


int main(){
   
    cin>>n;

    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            cin>>map[i][j];
        }
    }


    go(1, 1, 1, 2);


    cout<<method<<endl;



    return 0;
}