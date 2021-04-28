#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

long long base[100005];

long long com[100005];
int N, M;
int main(){
    cin>>N;

    for (int i = 0; i < N; i++)
    {
        
        cin>>base[i];
    }
    sort(base, base+N);

    cin>>M;

    for (int i = 0; i < M; i++)
    {
        cin>>com[i];
    }
    int l, r, mid;

    for (int i = 0; i < M; i++)
    {
        l=0; r=N-1;
        bool check=false;
        while(l<=r){
            mid=(l+r)/2;
            //cout<<mid<<endl;

            if(base[mid]==com[i]){
                printf("%d\n", 1);
                check=true;
                break;
            }else if(base[mid]>com[i]){
                r=mid-1;
            }else{
                l=mid+1;
            }
        }

        if(!check) printf("%d\n", 0);
    
    }
   

    return 0;
}