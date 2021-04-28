#include <string>
#include <vector>
#include<algorithm>
#include<string>
#include<set>
#include<cmath>


using namespace std;

vector<char> s;

void getprime(int num, int sosu[]){
    

    for(int i=0; i<=num; i++){
        sosu[i]=0; 
    }
     sosu[0]=1;
     sosu[1]=1;
    
    for(int i=2; i<sqrt(num); i++){
        if(sosu[i]){
            continue;
        }
        for(int j=i+i; j<=num; j+=i){
            sosu[j]=1;
        }
        
    }
}




int solution(string numbers) {
    int answer = 0;
    string ho=numbers;
    sort(ho.begin(), ho.end(), greater<char>());
   
    int num2= stoi(ho);
    
    int *sosu = new int[num2+5];
    getprime(num2, sosu);
    
    set<int> s;
    sort(numbers.begin(), numbers.end());
    
    do{
        
        for(int i=1; i<=numbers.size(); i++){
            string tmp=numbers.substr(0, i);
            if(!sosu[stoi(tmp)]){
                s.insert(stoi(tmp));
            }
        }
            
        
        
    }while(next_permutation(numbers.begin(), numbers.end()));
  
        
    
    
    answer= s.size();
    
    return answer;
}