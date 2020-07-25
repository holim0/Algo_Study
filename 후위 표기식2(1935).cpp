#include<iostream>
#include<string>
#include<stack>

using namespace std;
int N;
double num[30];
stack<double> v;
int main(){


    cin>>N;

    string s;
    cin>>s;

    for (int i = 0; i < N; i++)
    {
        cin>>num[i];
    }

    for (int i = 0; i < s.size(); i++)
    {
        if(s[i]=='+'||s[i]=='-'||s[i]=='*'||s[i]=='/'){
            double a, b;
            switch (s[i])
            {
            case '+':
                a=v.top(); v.pop();
                b=v.top(); v.pop();
                v.push(a+b);
                break;
            case '-':
                a=v.top(); v.pop();
                b=v.top(); v.pop();
                v.push(b-a);
                break;
            case '*':
                a=v.top(); v.pop();
                b=v.top(); v.pop();
                v.push(a*b);
                break;
            case '/':
                a=v.top(); v.pop();
                b=v.top(); v.pop();
                v.push(b/a);
                break;
            
            default:
                break;
            }

        }else{
            v.push(num[s[i]-65]);
        }
    }

    cout<<fixed;
    cout.precision(2);
    cout<<v.top()<<endl;

    return 0;
}