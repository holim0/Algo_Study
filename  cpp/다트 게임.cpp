#include <string>
#include <stack>
#include <string>


using namespace std;
stack<int> s1;
stack<char> s2;

int solution(string dartResult) {
    int answer = 0;
    
    for(int i=0; i<dartResult.size(); i++){
        if(isdigit(dartResult[i])){
            if(isdigit(dartResult[i+1])){
                s1.push(10);
                i+=1;
            }else{
            s1.push(dartResult[i]-'0');}
                
        }else if(dartResult[i]=='D' || dartResult[i]=='S'||dartResult[i]=='T'){
            s2.push(dartResult[i]);
            
        }else if(dartResult[i]=='#'){
            int tmp= s1.top(); s1.pop();
            if(s2.top()=='D'){
                tmp=tmp*tmp;
                s2.pop();
            }else if(s2.top()=='T'){
                tmp=tmp*tmp*tmp;
                s2.pop();
            }
                     
            s1.push(-tmp);
            s2.push('N');
            
        }else if(dartResult[i]=='*'){
            bool isfirst=true;
            int n1= s1.top(); s1.pop();
            int n2;
            if(s2.top()=='D'){
                n1=n1*n1;
                s2.pop();
            }else if(s2.top()=='T'){
                n1=n1*n1*n1;
                s2.pop();
            }
            
            if(!s1.empty()){
                isfirst=false;
                 n2= s1.top(); s1.pop();
                if(s2.top()=='D'){
                    n2=n2*n2;
                    s2.pop();
                }else if(s2.top()=='T'){
                    n2=n2*n2*n2;
                    s2.pop();
                }
            }
            
            if(!isfirst){
                s1.push(2*n2); s1.push(2*n1);
                s2.push('N'); s2.push('N'); 
            }else{
                s1.push(2*n1); s2.push('N');
            }
        }
    }
    
    while(!s1.empty()){
        int tmp= s1.top(); s1.pop();
        
        if(s2.top()=='D'){
            answer+=tmp*tmp;
            s2.pop();
        }else if(s2.top()=='T'){
            answer+=tmp*tmp*tmp;
            s2.pop();
        }else{
            answer+=tmp;
            s2.pop();
        }
    }
    
    
    return answer;
}