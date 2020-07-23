#include<iostream>
#include<algorithm>
#include<string>
#include<set>

using namespace std;

int n, k;

int card[11];

set<string> s;

int main(){

    cin>>n>>k;

    for (int i = 0; i < n; i++)
    {
        cin>>card[i];
    }
    sort(card, card+n);
    do{
        string val="";

        for (int i = 0; i < k; i++)
        {
            val+=to_string(card[i]);
        }
        
        s.insert(val);
        
        
    }while(next_permutation(card, card+n));

    

    cout<<s.size()<<endl;


    return 0;
}