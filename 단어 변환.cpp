#include <string>
#include <vector>

using namespace std;
int minval=987654321;
bool visit[55]={false, };
string target2="";
void go(string cur, vector<string>words, int movcnt){
    
    if(cur==target2){
        minval = minval>movcnt ? movcnt : minval;
        return;
    }
    
    for(int i=0; i<words.size(); i++){
        int cnt=0; 
        string tmp=words[i];
        for(int j=0; j< cur.size(); j++){
            
                if(cur[j]!=tmp[j]) cnt++;
        }
        
        if(cnt==1 && !visit[i]){
            visit[i]=true;
            go(tmp, words, movcnt+1);
            visit[i]=false;
        }
    
        
        
    }
    
    
}


int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    bool ishere=false;
    target2=target;
    for(int i=0; i<words.size(); i++){
        if(target==words[i]){
            ishere=true;
        }
    }
    if(!ishere) return 0;
    
    go(begin, words, 0);
    
    answer= minval;
    return answer;
}