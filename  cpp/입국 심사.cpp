#include <string>
#include <vector>
#include <algorithm>


using namespace std;

unsigned long long solution(int n, vector<int> times) {
    unsigned long long answer = 0;
    unsigned long long valmin= n * times[times.size()-1];
    
    sort(times.begin(), times.end());
    unsigned long long left=1; unsigned long long right= n * times[times.size()-1];
    unsigned long long mid;  unsigned long long sum;
    while(left<=right){
        mid = (left+right)/2;
        sum=0; 
        for(int i=0; i<times.size(); i++){
            sum += mid/times[i];
        }
        
       
        if(sum>=n){
            valmin= min(valmin, mid);
            right= mid-1;
        }else if(sum<n){
            left= mid+1;
        }
        
    }
    
    answer= valmin;
    return answer;
}