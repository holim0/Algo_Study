#include<iostream>
#include<cmath>


using namespace std;

int T;
int a, b, e, f, n;

struct Circle{
    
    int x, y, r;
    bool check=false;
};

Circle c[51];

int solution(){


    int out1=0;
    int out2=0;
    int twice=0;

    for (int i = 0; i < n; i++)
    {
        long long d1 = pow(c[i].x-a, 2) + pow(c[i].y-b, 2);

        if(d1< pow(c[i].r, 2)){
            if(!c[i].check){
                c[i].check=true;
                out1++;
            }
        }

        long long d2= pow(c[i].x-e, 2) + pow(c[i].y-f, 2);

        if(d2< pow(c[i].r, 2)){
            if(!c[i].check){
                c[i].check=true;
                out2++;
            }else{
                twice++;
            }
        }

    }
    

    return out1+out2-twice;
}

int main(){

    
    cin>>T;
    
    while(T--){

        cin>>a>>b>>e>>f>>n;

        for (int i = 0; i < n; i++)
        {
            cin>>c[i].x>>c[i].y>>c[i].r;
            c[i].check=false;
        }
        
        cout<<solution()<<endl;


    }


    return 0;
}