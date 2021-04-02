function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    if(A.length===1){
        return 0;
    }
    var answer= 0;

    var fromStart =[];
    var fromEnd = [];
    var cnt ={}
    var curleader;
    var maxVal= -1;
    for(var i =0; i<A.length; i++){
        if(i===0){
            fromStart[0]=A[i];
            cnt[A[i]]=1;
            curleader=A[i];
            maxVal=1
        }else{
            if(A[i] in cnt){
                cnt[A[i]]+=1;
                if(cnt[A[i]]> (i+1)/2){
                    curleader=A[i];
                    fromStart[i]=curleader;
                    maxVal=cnt[A[i]];
                }else{
                    fromStart[i]=curleader;
                }
            }else{
                cnt[A[i]]=1;
                if(maxVal> (i+1)/2){
                    fromStart[i]= curleader;
                }else{
                    fromStart[i] =-1;
                }
            }   
        }
    }
    cnt ={};
    curleader = undefined;
    maxVal = -1;
    for(var i =A.length-1; i>=0; i--){
        if(i===A.length-1){
            fromEnd[i]=A[i];
            cnt[A[i]]=1;
            curleader=A[i];
            maxVal=1
        }else{
            if(A[i] in cnt){
                cnt[A[i]]+=1;
                if(cnt[A[i]]> (A.length-i)/2){
                    curleader=A[i];
                    fromEnd[i]=curleader;
                    maxVal=cnt[A[i]];
                }else{
                    fromEnd[i]=curleader;
                }
            }else{
                cnt[A[i]]=1;
                if(maxVal> (A.length-i)/2){
                    fromEnd[i]= curleader;
                }else{
                    fromEnd[i] =-1;
                }
            }   
        }
    }
    //  console.log(fromStart, fromEnd);
    for(var i=0; i<A.length-1; i++){
        if(fromStart[i]===fromEnd[i+1] && fromStart[i] !==-1 && fromEnd[i+1]!==-1){
            answer+=1;
        }
    }



    return answer;

}

[4, 4, 2, 5, 3, 4, 4, 4] 