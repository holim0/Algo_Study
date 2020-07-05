#include <string>
#include <vector>
#include<algorithm>


using namespace std;
vector<string> tmp2;
bool visit[10005]={false, };
vector<string> answer;
vector<vector<string>> tmp;

void go(vector<vector<string>> tickets,string start, int cnt){
    
    
    tmp2.push_back(start);
    
    if(cnt==tickets.size()){
        tmp.push_back(tmp2);
        return;
    }
    
    
    
    for(int i=0; i< tickets.size(); i++){
        if(tickets[i][0]==start && !visit[i]){
            visit[i]=true;
            go(tickets, tickets[i][1], cnt+1);
            visit[i]=false;
            tmp2.pop_back();
            
        }
       
    }
    
    
}


vector<string> solution(vector<vector<string>> tickets) {
   
    
    
    sort(tickets.begin(), tickets.end());
    
    go(tickets, "ICN", 0);
    
    sort(tmp.begin(), tmp.end());
    
    
    answer=tmp[0];
    
    return answer;
}