#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;
    int len= heights.size();
    
    for(int i=len-1; i>=0; i--){
        bool push=false;
        for(int j=i-1; j>=0; j--){
            if(heights[j]>heights[i]){
                push=true;
                answer.push_back(j+1);
                break;
            }
        }
        if(!push){
            answer.push_back(0);
        }
    }
    
    reverse(answer.begin(), answer.end());
    
    return answer;
}