#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
int N;
int map[52][11];
 
bool check[12]={false, };
vector<int> v;  //조합용 벡터
bool ru[4]={false, };
int order[11];
int maxresult=-1;

void playBase(){
    
    int outcnt;
    int cur=1;
    int point=0; 
    for(int i=1; i<=N; i++){
        outcnt=0;
        bool ru[4]={false, };
        while(outcnt<3){
            // cout<<cur<<endl;
            int tmp=map[i][v[cur-1]];
            if(tmp==0){
                outcnt++;
                // cout<<"아웃: "<<outcnt<<endl;
            }
            else{
                for(int k=3; k>=1; k--){
                    if(ru[k]==true){
                        if(k+tmp>3) {
                            ru[k]=false;
                            point++;
                        }
                        else{
                            ru[k]=false;
                            ru[k+tmp]=true;
                        }
                    }else {continue;}
                }
                if(tmp>3){
                    point++;
                }else{
                    ru[tmp]=true;
                }  
            }
            cur++;
            if(cur==10) {cur=1;}
        }
        
    }
    
    maxresult=max(point, maxresult); 
    return;       

    



}


void getJohab(int cnt){
    if(cnt==9){
        if(v[3]!=1) {
            return;
        }
        // for(int i=0; i<v.size(); i++){
        //     cout<<v[i]<<" ";
        // }
        // cout<<"\n";
        playBase();
        return;
    }

    for(int i=1; i<10; i++){
        if(!check[i]){
            check[i]=true;
            v.push_back(order[i]);
            getJohab(cnt+1);
            check[i]=false;
            v.pop_back();
        }
    }

}

int main(){
    cin>>N;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j < 10; j++)
        {
            cin>>map[i][j];
        }
        
    }

    for(int i=1; i<10; i++){
        order[i]=i;
    }

    getJohab(0); 

    
    cout<<maxresult<<endl;

    return 0;
}