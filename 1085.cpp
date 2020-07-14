#include<iostream>


using namespace std;

int x, y, w, h;
int main(){

    cin>>x>>y>>w>>h;

    int n[4];
    int result=98765432;
    n[0]=x; n[1]=y; n[2]=w-x; n[3]=h-y;

    for(int i=0; i<4; i++){
        result= result> n[i] ? n[i] : result;
    }

    cout<<result<<endl;

    return 0;
}