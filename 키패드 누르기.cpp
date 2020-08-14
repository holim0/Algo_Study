#include <string>
#include <vector>
#include <cmath>

using namespace std;
struct right {
    int x, y;
};

struct left {
    int x, y;
};

struct keypad {
    int x, y;
};
string solution(vector<int> numbers, string hand) {
    string answer = "";
    int n=1;
    keypad keypad[10];
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            keypad[n].x=i;
            keypad[n].y=j;
            n++;
        }
    }
    keypad[0].x=3;
    keypad[0].y=1;
    
    right r;
    left l;
    
    l={3, 0};
    r={3, 2};
    
    
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i]==1 || numbers[i]==4 || numbers[i]==7){
            int val=numbers[i];
            l={keypad[val].x, keypad[val].y};
            answer+="L";
        }else if(numbers[i]==3 || numbers[i]==6 || numbers[i]==9){
            int val=numbers[i];
            r={keypad[val].x, keypad[val].y};
            answer+="R";
        }else{
            int val=numbers[i];
            int ld=abs(l.x-keypad[val].x)+abs(l.y-keypad[val].y);
            int rd=abs(r.x-keypad[val].x)+abs(r.y-keypad[val].y);
            if(ld>rd){
                answer+="R";
                r={keypad[val].x, keypad[val].y};
            }else if(ld<rd){
                answer+="L";
                l={keypad[val].x, keypad[val].y};
            }else{
                if(hand=="right"){
                    answer+="R";
                    r={keypad[val].x, keypad[val].y};
                }else{
                    answer+="L";
                    l={keypad[val].x, keypad[val].y};
                }
            }
        }
    }
    
    
    
    
    return answer;
}