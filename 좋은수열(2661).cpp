#include<iostream>
#include<string>
#include<vector> 
#include<algorithm>

using namespace std;

vector<string> v;
int N;

bool check(string val){
    int size=val.size();
    for (int i = 1; i <= size/2; i++)
    {
        for (int j = 0; j < size-i; j++)
        {
            string s1=""; string s2="";
            for(int k=j; k<j+i; k++){
                s1+=val[k];
            }
            for (int k = j+i; k <j+i+i; k++)
            {
                s2+=val[k];
            }
            
            if(s1==s2) return false;
        }
    }
    
    return true;
}

void go(int cnt, string val){

    if(cnt==N){
        cout<<val<<endl;
        exit(0);
    }


    for (int i = 1; i <=3; i++)
    {
        if(check(val+to_string(i))){
            go(cnt+1,val+to_string(i));
        }
        
    }
    
}

int main(){
    
    cin>>N;

    go(1, "1");

    return 0;
}