#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> stones, int k) {
    int answer = 0;
    
    int l=1; 
    int maxval=-1;
    for(int i=0; i<stones.size(); i++){
        maxval=max(stones[i], maxval);
    }
    int r=maxval; int mid;
    
    while(l<=r){
        mid=(l+r)/2;
        bool flag=false;
        int cnt=0;
        for(int i=0; i<stones.size(); i++){
            int val=stones[i]-mid;
            if(val<=0){
                cnt+=1;
                if(cnt==k){
                    flag=true; 
                    break;
                }
            }else{
                cnt=0;
            }
        }
        if(!flag){
            l=mid+1;
        }else{
            answer=mid;
            r=mid-1;
        }
    }
    
    return answer;
}