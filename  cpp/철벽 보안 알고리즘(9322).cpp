#include<iostream>
#include<string>

using namespace std; 

int tc;
string open1[1005];
string open2[1005];
string sec[1005];
int idx[1005];
string result[1005];
int main(){

    cin>>tc;
    int n;
    while(tc--){
        
        cin>>n;
        for (int i = 0; i < n; i++)
        {
            cin>>open1[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin>>open2[i];
        }
        for(int i=0; i<n; i++){
            for (int j = 0; j < n; j++)
            {
                if(open2[i]==open1[j]){
                    idx[i]=j;
                }
            }
        }

        
        for (int i = 0; i < n; i++)
        {
            cin>>sec[i];
            result[idx[i]]=sec[i];
            
        }

        for (int i = 0; i < n; i++)
        {
            cout<<result[i]<<" ";
        }
    

    }

    return 0;
}

