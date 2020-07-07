#include <string>
#include <vector>


using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> bagu;
    int cur;
    for(int i=0; i<moves.size(); i++){
        cur= moves[i]-1;
        
        for(int i=0; i<board.size(); i++){
            if(board[i][cur]!=0){
                if(!bagu.empty() && board[i][cur]==bagu.back()){
                    bagu.pop_back();
                    answer+=2;
                }else{
                    bagu.push_back(board[i][cur]);
                }
                board[i][cur]=0;
                break;
            }
        }
        
    }
    
    
    
    
    return answer;
}