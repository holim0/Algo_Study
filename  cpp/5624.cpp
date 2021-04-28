#include<iostream>
#include<vector>

using namespace std;

int N;
int num[5005];
bool check[400000];


int main(){


    cin>>N;
    int result=0;

    for (int i = 0; i < N; i++)
    {
        cin>>num[i];
    }

    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if(check[num[i]-num[j]+200000]){
                result++;
                break;
            }
        }

        for (int j = 0; j <=i; j++)
        {
            check[num[i]+num[j]+200000]=true;
        }
        
        
        
    }
    
    cout<<result<<endl;



    return 0;
}