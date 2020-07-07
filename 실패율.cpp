#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(pair <double, int> &a, pair<double, int> &b){
    if(a.first==b.first){
        return a.second<b.second;
    }
    
    return a.first>b.first;
    
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<double, int>> tmp;
    double cnt;
    double base;
    
   for(int j=1; j<=N; j++){
        cnt=0; 
        base=stages.size();
        for(int i=0; i<stages.size();){
            if(j==stages[i]) {
                cnt++;
                stages.erase(stages.begin()+i);
            }else{
                i++;
            }
            
                
        }
       if(cnt==0){
           tmp.push_back({0, j});
       }else{
       tmp.push_back({cnt/base,j});}
       
       
   }
    sort(tmp.begin(), tmp.end(),cmp);
    
    for(int i=0; i<tmp.size(); i++){
        answer.push_back(tmp[i].second);
    }
    
    return answer;
}