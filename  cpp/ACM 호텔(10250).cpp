#include<iostream>

using namespace std;
int map[101][101];

int main(){

    int tc;
    cin>>tc;
    int floor, ho;
    while(tc!=0){
        int h, w, n;
        cin>>h>>w>>n;

        if(n%h==0){
            floor=h;
            ho=n/h;
        }else{
            floor=n%h;
            ho=n/h+1;
        }
        

        string s1=to_string(floor);
        string s2=to_string(ho);

        if(s2.size()==1){
            cout<<s1+'0'+s2<<endl;
        }
        else{
            cout<<s1+s2<<endl;
        }
        tc--;

    }


    return 0;
}