#include <string>
#include <vector>
#include <string>

using namespace std;



vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    int tmp;
    string val="";
    string val2="";
    for(int i=0; i<n; i++){
        tmp = arr1[i] | arr2[i];
        val=""; val2= "";
        while(1){
            if(tmp%2==0){
                val+="0";
                
            }else{
                val+="1";
            }
            tmp/=2;
            
            if(tmp==0) break;
            
        }
        
        for(int j=val.size(); j<n; j++){
            val+="0";
            
        }
        
        for(int k=n-1; k>=0; k--){
            if(val[k]=='1'){
                val2+="#";
            }else{
                val2+=" ";
            }
        }
            
        
        
        answer.push_back(val2);
        
    }
    
    return answer;
}