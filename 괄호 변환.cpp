#include <string>
#include <vector>
#include <stack>

using namespace std;
 string u="", v="";
vector<string> saveu;

string answer="";

bool check(string s){
    stack<char> st;
    
    for(int i=0; i<s.size(); i++){
        if(s[i]=='(') st.push(s[i]);
        else{
            if(!st.empty()) {
                st.pop();
            }
            
        }
    }
    
    if(!st.empty()) return false;
    return true;
}

void divide(string s){
    
    int n1=0, n2=0; 
    u=""; v="";
    for(int i=0; i<s.size(); i++){
        if(s[i]=='(') {
            u+='(';
            n1++;
        }
        else {
            u+=')';
            n2++;
        }
        
        if(n1==n2){
            if(i==s.size()-1){
                v="";
                break;
            }
            v=s.substr(i+1, s.size()-i-1);
            break;
        }
    }
    
    if(check(u)){
        answer+=u;
        u="";
        if(v!="") divide(v);
        else return;
    }else{
        saveu.push_back(u);        
        answer+='(';
        if(v!=""){divide(v);}
        answer+=')';
        string tmp="";
        string tmp2=saveu.back();
        if(tmp2.size()>2){
            for(int i=1; i<tmp2.size()-1; i++){
                if(tmp2[i]=='('){
                    tmp+=')';
                }else{
                    tmp+='(';
                }
            }
        }
        answer+=tmp;
        saveu.pop_back();
        return;
        
    }
    
    
}

string solution(string p) {
   
    if(p=="") return "";
    else if(check(p)){
        return p;
    }
    
    divide(p);
      
    
        
    return answer;
}