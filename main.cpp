#include <string>
#include <vector>
#include <algorithm>
#include<iostream>


using namespace std;

int solution(vector<int> budgets, int M) {
    int answer = 0;
    
    
    
    int left= 1; int right= M;
    
    int mid; int tmp;
    while(1){
        tmp=0;
        mid=(left+right)/2;

        cout<<mid<<endl;
        
        if(mid==left || mid==right){
            answer=mid; 
            break;
        }
        
        for(int i=0; i< budgets.size(); i++){
            if(mid<budgets[i]){
                tmp+=mid;
            }else{
                tmp+=budgets[i];
            }
        }
        
        cout<<"tmp:"<<tmp<<endl;
        

        if(tmp >= M){
            right=mid-1;
            cout<<"right: "<<right<<endl;
            
        }else{
            left= mid+1;
        }
         
        
    }
    
    
    return answer;
    
}

int main(){

    vector<int> budgets;

    budgets.push_back(120);
    budgets.push_back(110);
    budgets.push_back(140);
    budgets.push_back(150);


    cout<<solution(budgets, 485);



    return 0;

}