#include <string>
#include <vector>


using namespace std;

vector<int> n1{1,2,3,4,5};
vector<int> n2{2,1,2,3,2,4,2,5};
vector<int> n3{3,3,1,1,2,2,4,4,5,5};

int max(int a, int b){
    return a < b ? b : a;
}

vector<int> solution(vector<int> answers) {
    int value = 0;
    vector<int> answer;
    vector<int> count(3);

    for(int i = 0; i < answers.size() ; i++){
        if(n1[i % n1.size()] == answers[i]) count[0]++;
        if(n2[i % n2.size()] == answers[i]) count[1]++;
        if(n3[i % n3.size()] == answers[i]) count[2]++;
    }

    value = max(max(count[0],count[1]),count[2]);

    for(int i = 0; i < 3; i++)
        if(count[i] == value) answer.push_back(i+1);

    return answer;
}