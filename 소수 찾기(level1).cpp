#include <string>
#include <vector>
#include<cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    int *sosu= new int[n+5];
    for(int i=0; i<=n; i++){
        sosu[i]=0;
    }
    
    sosu[0]=1;
    sosu[1]=1;
    
    for(int i=2; i<sqrt(n); i++){
        if(sosu[i]) {continue;}
        
        for(int j=i+i; j<=n; j+=i){
            sosu[j]=1;
        }
        
    }
    
    for(int i=1; i<=n; i++){
        if(!sosu[i]) answer++;
    }
    
    
    return answer;
}