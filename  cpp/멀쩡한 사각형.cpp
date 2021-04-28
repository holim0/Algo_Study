using namespace std;

long long gcd(long long a, long long b){
    
    while(b!=0){
        long long r=a%b;
        a=b;
        b=r;
    }
    
    return a;
}

long long solution(int w,int h) {
    long long answer = 1;
    
    long long total=(long long)w*(long long)h;
    
    long long val=gcd(w, h);
    
    answer=total-(w+h-val);
    
    
    
    return answer;
}