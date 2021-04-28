#include<iostream>
#define MAX 1000000+5
#include<algorithm>

using namespace std;

int N, M;
long long len[MAX];
long long  maxTree=-1;
long long  answer;
int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        cin>>len[i];
        maxTree=max(maxTree, len[i]);
    }  

    sort(len, len+N);

    long long left=1;
    long long right=maxTree;
    long long mid, sum;
    while(left<=right){
        mid=(left+right)/2;
        sum=0;
        //cout<<mid<<endl;

        for (int i = 0; i < N; i++)
        {
            if(mid<len[i]){
                sum+=len[i]-mid;
            }
        }
        //cout<<sum<<endl;
        if(sum>=M){
            answer=mid;
            left=mid+1;
        }else{
            right=mid-1;
        }
    }

    cout<<answer<<endl;

    return 0;
}