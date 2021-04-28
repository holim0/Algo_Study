#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int n, score, p;    
vector<int> v;

bool comp(int a, int b){

    return a>b;
}
int main(){


    cin>>n>>score>>p;

    for (int i = 0; i < n; i++)
    {
        int n1; cin>>n1;
        v.push_back(n1);
    }
    
    if(v.size()==p){
        bool flag=false;
        for (int i = 0; i < v.size(); i++)
        {
            if(score>v[i]){
                flag=true;
                break;
            }
        }

        if(flag){
            v.push_back(score);
            sort(v.begin(), v.end(), comp);
            // for (int i = 0; i < v.size(); i++)
            // {
            //     cout<<v[i]<<" ";
            // }
            
            for (int i = 0; i < v.size(); i++)
            {
                if(score==v[i]){
                    cout<<i+1<<endl;
                    break;
                }
            }
            
        }else{
            cout<<-1<<endl;
        }
        

    }else{
        v.push_back(score);
        sort(v.begin(), v.end(), comp);
        for (int i = 0; i < v.size(); i++)
        {
            if(score==v[i]){
                cout<<i+1<<endl;
                break;
            }
        }
        
    }
    

    return 0;
}