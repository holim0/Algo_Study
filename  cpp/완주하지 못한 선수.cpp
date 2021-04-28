#include <string>
#include <vector>
#include <set>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    bool check[100005]={false, };
    multiset<string> s;
    
    for(int i=0; i<participant.size(); i++){
        s.insert(participant[i]);
    }  
        
   
    for(int i=0; i<completion.size(); i++){
        auto itr= s.find(completion[i]);
        s.erase(itr);
    }    
        
        
        
        auto idx= s.begin();
    
    answer= *idx;
    
    
   
    return answer;
}