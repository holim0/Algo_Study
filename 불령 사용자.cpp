#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;
set<string> list;
vector<string> list2;
vector<string> tmp;
bool check[10]={false, };
int result=0;
vector<vector<string>> v;
set<vector<string>> s;

bool isSame(string a, string b){
    
    if(a.size()!=b.size()) return false;
    
    for(int i=0; i<a.size(); i++){
        if(a[i]!=b[i] && a[i]!='*') return false;
    }
    
    return true;
    
}

void dfs(int cnt, int target, vector<string> ban){
    
   if(cnt==target){
       for(int i=0; i<tmp.size(); i++){
           if(!isSame(ban[i], tmp[i])) return;
       }
       v.push_back(tmp);
       return;
   }
    
    
   for(int i=0; i<list2.size(); i++){
       if(!check[i]){
           check[i]=true;
           tmp.push_back(list2[i]);
           dfs(cnt+1, target, ban);
           check[i]=false;
           tmp.pop_back();
       }
   }
    
}


int solution(vector<string> user_id, vector<string> banned_id) {
    int answer = 0;
    int banSize=banned_id.size();
    for(int i=0; i<banned_id.size(); i++){
        for(int j=0; j<user_id.size(); j++){
            if(isSame(banned_id[i], user_id[j]) && !check[j]){
                list.insert(user_id[j]);
            }
        }
    }
    
    set<string>:: iterator iter;
    for(iter=list.begin(); iter!=list.end(); iter++){
        list2.push_back(*iter);
    }
    dfs(0, banSize, banned_id);
    
    for(int i=0; i<v.size(); i++){
        sort(v[i].begin(), v[i].end());
        s.insert(v[i]);
    }
    
    answer=s.size();
    return answer;
}