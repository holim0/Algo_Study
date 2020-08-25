#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int cube[11];
int start=0;
int result=-1;
bool done[5]={false, };
bool check[5][45];

struct horse{
    int curRoot=1;
    int curLoca=0;
    bool finish=false;
    int score=0;
};

horse h[5];

int root[5][30]={
    {0, }, 
    {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, },
    {0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40, },
    {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40, },
    {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40, }
};


bool doubleCheck(int root, int loca, int val){

    if(root==1){
        if(val==10){
            if(check[1][5] || check[2][5] || check[3][5] || check[4][5]) return true;

        }else if(val==20){
            if(check[1][10] || check[3][10] || check[4][10]) return true;

        }else if(val==30){
            if(check[1][15] || check[4][15]) return true;
        }else if(val==40){
            if(check[1][20] || check[2][12] || check[3][16] || check[4][22]) return true;   
        }
        else{
            if(check[root][loca]) return true;
        }

    }else{
        if(val==25){
            if(check[2][9] || check[3][13] || check[4][19]) return true;
        }else if(val==30){
            if(check[2][10] || check[3][14] || check[4][20]) return true;

        }else if(val==35){
            if(check[2][11] || check[3][15] || check[4][21]) return true;
        }else if(val==40){
            if(check[1][20] || check[2][12] || check[3][16] || check[4][22]) return true; 
        }else{
            if(check[root][loca]) return true;
        }

    }

    return false;

}



void move(int idx){
    
    if(idx>=11){
        int sum=0;
        for (int i = 1; i <=4; i++)
        {
            sum+=h[i].score;
        }
        result=max(result, sum);
        return;
    }


    int nextLoca, nextVal;
    

    for (int i = 1; i <= 4; i++)
    {   
        if(h[i].finish) continue;
        horse tmp=h[i];
        
        nextLoca=h[i].curLoca+cube[idx];
        nextVal=root[h[i].curRoot][nextLoca];
                
                if(h[i].curRoot==1){
                    if(nextVal==10 || nextVal==20 || nextVal==30 || nextVal==40){
                        if(!doubleCheck(h[i].curRoot, nextLoca, nextVal)){
                            check[h[i].curRoot][h[i].curLoca]=false;
                            if(nextVal!=40) { h[i].curRoot=nextVal/10+1; }
                            h[i].score+=nextVal;
                            h[i].curLoca=nextLoca;
                            check[h[i].curRoot][h[i].curLoca]=true;

                            move(idx+1);

                            check[h[i].curRoot][h[i].curLoca]=false;
                            h[i]=tmp;
                            check[h[i].curRoot][h[i].curLoca]=true;
                        }
                    }else{
                        if(!doubleCheck(h[i].curRoot, nextLoca, nextVal)){
                            check[h[i].curRoot][h[i].curLoca]=false;
                            h[i].curLoca=nextLoca;
                            
                            if(root[1][h[i].curLoca]==0){
                                h[i].finish=true;
                            }else{
                                check[h[i].curRoot][h[i].curLoca]=true;
                                h[i].score+=nextVal;
                            }
                            move(idx+1);
                            
                            check[h[i].curRoot][h[i].curLoca]=false;
                            h[i]=tmp;
                            check[h[i].curRoot][h[i].curLoca]=true;
                        }
                    }

                }else{
                    if(!doubleCheck(h[i].curRoot, nextLoca, nextVal)){
                        check[h[i].curRoot][h[i].curLoca]=false;
                        h[i].curLoca=nextLoca;

                        if(root[h[i].curRoot][h[i].curLoca]==0){
                            h[i].finish=true;
                        }else{
                            h[i].score+=nextVal;
                            check[h[i].curRoot][h[i].curLoca]=true;
                        }
                        move(idx+1);
                        
                        check[h[i].curRoot][h[i].curLoca]=false;
                        h[i]=tmp;
                        check[h[i].curRoot][h[i].curLoca]=true;
                    }
                }
            
        }    
}



int main(){

    for (int i = 1; i <=10; i++)
    {
        cin>>cube[i];
    }
    
    move(1);
    
    cout<<result<<endl;

    return 0;
}