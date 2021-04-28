#include<iostream>
#include<queue>

using namespace std;

queue<int> q;
int N;
int main(){

    cin>>N;

    for (int i = 1; i <=N; i++)
    {
        q.push(i);
    }
    int val;
    while(q.size()!=1){

        q.pop();
        val=q.front();
        q.pop();
        q.push(val);
    }


    cout<<q.front()<<endl;



    return 0;
}