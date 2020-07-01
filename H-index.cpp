#include <string>
#include <vector>
#include <algorithm>

using namespace std;



int solution(vector<int> citations) {
    int answer = 0;
    int len=citations.size();
   
    
    
   while(1){
       int up=0; int down=0; 
       
       for(int i=0; i<len; i++){
           if(citations[i]>=answer){
                up++;
           }else if(citations[i]<=answer){
               down++;
           }
       }
       
       if(up>=answer && down<=answer){
           answer++;
       }else{
           break;
       }
   }
    
    
    
    
    return answer-1;
}