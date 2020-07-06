#include <string>
#include <vector>
#include<string>
#include<iostream>



using namespace std;
int minlen=987654321;


void small(string s, int cnt){
    
    string tmp="";
    string base=s.substr(0, cnt);
    string val="";
    int num=0; 
    for(int i=0; i<s.size(); i+=cnt){
        val= s.substr(i, cnt);
        cout<<val<<endl;
        
        if(base==val){
            num++;
            cout<<num<<endl;
        }
        else{
            if(num==1){
                tmp+=base;
                cout<<tmp<<endl;
            }else if(num>1){
                tmp+=to_string(num); tmp+=base;
                cout<<tmp<<endl;
            }
            base=s.substr(i, cnt);
            num=1;
            
        }

        if(i+cnt==s.size() || base.size()!=cnt){
            if(num==1) {tmp+=base;}
            else if(num>1){ tmp+=to_string(num); tmp+=base;}

            cout<<tmp<<endl;
            break;
        }
        


    
         
        
    }
    
    minlen= minlen>tmp.size() ? tmp.size(): minlen;
    cout<<"min:" <<minlen<<endl;
    
}


int solution(string s) {
    int answer = 0;
    
    for(int i=1; i<=s.size(); i++){
        small(s, i);
    }
    
    
    answer=minlen;
    
    return answer;
}

