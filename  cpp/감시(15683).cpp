#include<iostream>
#include<vector>

using namespace std;

int N, M;

char map[10][10];
char copymap[10][10];
int cctv=0;
int result=987654321;
vector<int> v;

vector<pair<int, pair<int, int>>> location;

void goleft(int x, int y){  // 왼쪽으로 가면서 감시
    
    for(int i=y-1; i>=0; i--){
        if(copymap[x][i]=='6') return;
        if(copymap[x][i]=='0'){
            copymap[x][i]='#';
        }
    }

}

void goright(int x, int y){      //오른쪽 감시
    for(int i=y+1; i<M; i++){
        if(copymap[x][i]=='6') return;
        if(copymap[x][i]=='0'){
            copymap[x][i]='#';
        }
    }
}

void goup(int x, int y){      // 위쪽 감시
    for(int i=x-1; i>=0; i--){
        if(copymap[i][y]=='6') return;
        if(copymap[i][y]=='0'){
            copymap[i][y]='#';
        }
    }
}

void godown(int x, int y){        // 아래쪽 감시
    for(int i=x+1; i<N; i++){
        if(copymap[i][y]=='6') return;
        if(copymap[i][y]=='0'){
            copymap[i][y]='#';
        }
    }
}


int getCnt(){           /// 0의 개수 카운트

    int sum=0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if(copymap[i][j]=='0') sum++;
        }
    }
    //cout<<"sum:"<<sum<<endl;
    return sum;
}

void Copy(){     //기존 배열 복제

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            copymap[i][j]=map[i][j];
        }
    }
    
}

void getResult(){
    
    int cctval; int x, y;  
    for (int i = 0; i < v.size(); i++)
    {   
        cctval=location[i].first;     //cctv 의 종류
        x=location[i].second.first;
        y=location[i].second.second;
        int t=v[i]; // 1일땐 그대로 2, 3, 4는 차례대로 시계방향으로 화살표 돌리기
        switch (t)
        {
        case 1:          //       그대로
            switch (cctval)
            {
            case 1:
                goright(x, y);
                break;
            case 2:
                goleft(x, y);
                goright(x, y);
                break;
            case 3:
                goup(x, y);
                goright(x, y);
                break;
            case 4:
                goup(x, y);
                goright(x, y);
                goleft(x, y);
                break;
            case 5:
                goup(x, y);
                godown(x, y);
                goright(x, y);
                goleft(x, y);
                break;
            
            }
            break;
        case 2:         //       왼쪽 한번
            switch (cctval)
            {
            case 1:
                godown(x, y);
                break;
            case 2:
                godown(x, y);
                goup(x, y);
                break;
            case 3:
                goright(x, y);
                godown(x, y);
                break;
            case 4:
                goup(x, y);
                godown(x, y);
                goright(x, y);
                break;
            case 5:
                goup(x, y);
                godown(x, y);
                goright(x, y);
                goleft(x, y);
                break;
            
            }
            break;
        case 3:        // 왼쪽 두번
            switch (cctval)
            {
            case 1:
                goleft(x, y);
                break;

            case 2:
                goleft(x, y);
                goright(x, y);
                break;
            case 3:
                goleft(x, y);
                godown(x, y);
                break;
            case 4:
                goright(x, y);
                godown(x, y);
                goleft(x, y);
                break;
            case 5:
                goup(x, y);
                godown(x, y);
                goright(x, y);
                goleft(x, y);
                break;
            
            }
            break;
        case 4:           // 왼쪽 세번
            switch (cctval)
            {
            case 1:
                goup(x, y);
                break;

            case 2:
                goup(x, y);
                godown(x, y);
                break;
            case 3:
                goleft(x, y);
                goup(x, y);
                break;
            case 4:
                goup(x, y);
                godown(x, y);
                goleft(x, y);
                break;
            case 5:
                goup(x, y);
                godown(x, y);
                goright(x, y);
                goleft(x, y);
                break;
            
            }
            break;
        
        
        }
    }
    


}

void go(int cnt){
    /// v 벡터에 1, 2, 3, 4 조합 넣어주기. 
    if(cnt==cctv){
        Copy();
        getResult();
        // for (int i = 0; i < v.size(); i++)
        // {
        //     cout<<v[i];
        // }
        // cout<<endl;
        
        // for (int i = 0; i < N; i++)
        // {
        //     for (int j = 0; j < M; j++)
        //     {
        //         cout<<copymap[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
        // cout<<endl;
        int val=getCnt();
        //cout<<val<<endl;
        result= result > val ? val : result;
        return;
    }

    
    for(int i=1; i<=4; i++){
        v.push_back(i);
        go(cnt+1);
        v.pop_back();
    }



}

int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin>>map[i][j];
        }
        
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if(map[i][j]!='0' && map[i][j]!='6') {
                cctv++;
                location.push_back({map[i][j]-'0', {i, j}});
            }
                
        }
        
    }

    
    go(0);

    cout<<result<<endl;


    return 0;
}