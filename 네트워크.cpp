#include <string>
#include <vector>

using namespace std;

bool visit[205]={false, };
int bound;
int answer2=0; 
void go(vector<vector<int>> computers,int x){
   
    
    for(int i=0; i<bound; i++){
        if(x==i){
            continue;
        }
        
        if(computers[x][i]==1 && !visit[i]){
            visit[i]=true;
            go(computers, i);
        }
    }
    
    
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    bound=n;
    
    
    for(int i=0; i<n; i++){
        if(!visit[i]){
            visit[i]=true;
            go(computers, i);
            answer++;
        }
        
    }
    
    
    return answer;
}