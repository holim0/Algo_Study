#include<iostream>
#define MAX 1000000+5
using namespace std;
int N;
int A[MAX];
int b, c;
long long result=0;

int main(){

    cin>>N;
    for (int i = 0; i < N; i++)
    {
        cin>>A[i];
    }
    cin>>b>>c;
    
    for (int i = 0; i < N; i++)
    {
        A[i]-=b; result+=1;
        if(A[i]<=0) continue;
        else{
            int val=A[i]%c;
            int val2=A[i]/c;
            if(val!=0){
                result+=val2+1;
            }else{
                result+=val2;
            }
        }
    }
    
    cout<<result<<endl;
    return 0;
}