#include<iostream>
#include<string>

using namespace std;
int num[200]={0,};
int main(){

    string s;
    cin>>s;

    for (int i = 0; i < s.size(); i++)
    {   
        //cout<<s[i]-'0'<<endl;
        if(s[i]-'0'>=49){
            num[s[i]-'0'-32]++;
        }
        else{
            num[s[i]-'0']++;
        }
    }
    bool flag=true;
    

        int maxidx;
        int result=-1;
        for (int i = 0; i < 50; i++)
        {
            if(result<num[i] &&num[i]!=0){
                result=num[i];
                maxidx=i;
            }
        }
        

        int cnt=0;
        for (int i = 0; i < 50; i++)
        {
            if(result==num[i]) cnt++;
        }

        if(cnt>1){
            cout<<"?"<<endl;
            return 0;
        }
        

        printf("%c\n", maxidx+48);

    return 0;
}