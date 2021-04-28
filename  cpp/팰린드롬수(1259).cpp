#include<iostream>
#include<string>

using namespace std;

string s;

bool pal(string s){

    int start=0; 
    int end= s.size()-1;


    while(start<=end){

        if(s[start]!=s[end]) return false;
        else{
            start++;
            end--;
        }
    }


    return true;


}


int main(){

    while(1){

        cin>>s;
        if(s=="0"){
            break;
        }
        
        if(pal(s)) {
            cout<<"yes"<<endl;
        }else{
            cout<<"no"<<endl;
        }

    }



    return 0;
}