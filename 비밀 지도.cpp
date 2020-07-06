#include <string>
#include <vector>
#include<string>
#include<iostream>


using namespace std;

string getprime(int size, int a, int b){
    
   int tmp = a | b;
    
    string val="";
    string val2="";
    if(tmp==0){
        val+='0';
    }else if(tmp==1){
        val+='1';
    }else{
    
        while(1){
            val+= to_string(tmp%2);
            tmp/=2;

            if(tmp==1){
                val+="1";
                break;
            }
        }
    }
    
    for(int i=size-1; i>=0; i--){
        if(val[i]=='1'){
            val2+="#";
        }
        else{
            val2+=" ";
        }
    }
    
    
    
    return val2;
}

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    
    
    for(int i=0; i<n; i++){
        answer.push_back(getprime(n,arr1[i], arr2[i]));
    }
    
    
    return answer;
}


int main(){

    vector<string> s;

    
    vector<int>arr1;
    vector<int> arr2;

    for(int i=0; i<5; i++){
        arr1.push_back(0);

    }

   
        arr2.push_back(30);
        arr2.push_back(1);
        arr2.push_back(21);
        arr2.push_back(17);
        arr2.push_back(28);
    

   s= solution(5, arr1, arr2);
    
    for(int i=0; i<s.size(); i++){
        cout<<s[i]<<endl;
    }
    

    return 0; 

}