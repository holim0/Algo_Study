#include<iostream>
#define MAX 1000000+1000000
#include<string>

using namespace std;

bool num[MAX+1]={false, };
int n;
void sosu(){

    num[0]=true;
    num[1]=true;

    for (int i = 2; i*i<=MAX; i++)
    {
        for (int j = i+i; j <=MAX; j+=i)
        {
            num[j]=true;
        }
        
    }

}


int main(){

    cin>>n;
    string val;

    sosu();
    for (int i = n; i <=MAX; i++)
    {  
        if(!num[i]){
            val = to_string(i);
            bool IsOut=false;
            for (int j = 0; j <= val.size()/2; j++)
            {
                if(val[j]!=val[val.size()-1-j]){
                    IsOut=true;
                    break;
                }
            }
            if(IsOut) continue;
            else{
                cout<<i<<endl;
                return 0;
            }
        }
        
        
    }
    


    return 0;
}