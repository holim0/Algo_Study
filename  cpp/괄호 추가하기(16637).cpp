#include<iostream>
#include<vector>
#include<climits>


using namespace std;


long long answer=LLONG_MIN;
vector<int> n;
vector<char> op;

long long cal(char op, long long n1, long long n2){
    if(op == '+')
        return n1+n2;
    else if(op == '-')
        return n1-n2;
    else
        return n1*n2;
}

void go(long long cur, int oppos){
     
    if(oppos>=op.size()){
        answer= cur >answer ? cur : answer;
        return;
    }


    long long tmp=cal(op[oppos], cur, n[oppos+1]);
    go(tmp, oppos+1);


    if(oppos+1<op.size()){
        long long tmp2=cal(op[oppos+1], n[oppos+1], n[oppos+2]);
        go(cal(op[oppos], cur, tmp2), oppos+2);
    }


}



int main(){
    
    int tc;
    string s;
    cin>>tc>>s;

    for(int i=0; i<s.size(); i++){
        if(s[i]=='+' || s[i]=='-' || s[i]=='*'){
            op.push_back(s[i]);
        }else{
            n.push_back(s[i]-'0');
        }
    }

    go(n[0], 0);

    

    cout<<answer<<endl;

    return 0;
}