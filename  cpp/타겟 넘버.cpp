#include <string>
#include <vector>


using namespace std;

int answer2=0;
int target2;

void go(vector<int> numbers, int start, int cnt, int dab){
    if(cnt == numbers.size()){
        if(target2==dab){
            answer2++;
        }
        return;
    }



        go(numbers, start+1, cnt+1, dab+numbers[start]);
        go(numbers, start+1, cnt+1, dab-numbers[start]);


}

int solution(vector<int> numbers, int target) {
    int answer = 0;

    target2= target;
    go(numbers, 0, 0, 0);

    answer=answer2;

    return answer;
}