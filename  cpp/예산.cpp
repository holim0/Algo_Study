#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> budgets, int M) {
    int answer = 0;
    int len=budgets.size();
    sort(budgets.begin(), budgets.end());
    int mid;
    int left= 1; int right= M;
    long long tmp;
    
    for(int i=0; i<len; i++){
        tmp+= budgets[i];
    }
    if(tmp<M){
        answer= budgets[len-1];
        return answer;
    }
   
    while(1){
        tmp=0;
        mid= (left+right)/2;
        
        if(mid== left){
            for(int i=0; i<len; i++){
                if(right>=budgets[i]){
                    tmp+=budgets[i];
                }else{
                    tmp+=right;
                }
            }
            
            if(tmp < M){
                answer=right; 
                break;
            }
            
            answer=mid;
            break;
            
        }
            
            
        
        
        
        for(int i=0; i<len; i++){
            if(mid>=budgets[i]){
                tmp+=budgets[i];
            }else{
                tmp+=mid;
            }
            
        }
        
        if(tmp < M){
            left=mid;
        }else if(tmp > M){
            right=mid;
        }else if(tmp == M){
            answer=mid;
            break;
        }
        
        
        
        
    }
   
    
    
    
    
    
    
    return answer;
    
}