#include<iostream>
#include<algorithm>

using namespace std;
int N, L;
int loca[1001];
int result=0;
int main(){

    cin>>N>>L;

    for (int i = 0; i < N; i++)
    {
        cin>>loca[i];
    }
    
    sort(loca, loca+N);
    int cur;
    int sum=0;
    for (int i = 0; i < N; i++)
    {   
        if(i==N-1){
            result++;
        }
        sum+=loca[i+1]-loca[i];
        if(sum<L) continue;
        else{
            sum=0; 
            result++;
        }
    }
    
    cout<<result<<endl;


    return 0;
}