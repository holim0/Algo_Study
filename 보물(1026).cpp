#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int N;

int a[55];
int b[55];

bool comp(int a, int b){
    
    return a>b;

}

int main(){

    cin>>N;
    
    for (int i = 0; i < N; i++)
    {
        cin>>a[i];
    }

    for (int i = 0; i < N; i++)
    {
        cin>>b[i];
    }

    sort(a, a+N);

    sort(b, b+N, comp);
    
    int s=0;

    for (int i = 0; i < N; i++)
    {
        s+=a[i]*b[i];
    }
    

    cout<<s<<endl;


    return 0;
}