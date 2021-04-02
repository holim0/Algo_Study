function solution(n, computers) {
    var answer = 0;

    var q = [];
    var check = new Array(n).fill(false);

    var cur;
    for (var idx = 0; idx < n; idx++) {
        if (check[idx] === false) {
            check[idx] = true;
            answer += 1;
            q.push(idx);
        }
        while (q.length > 0) {
            cur = q.shift();
            for (var i = 0; i < n; i++) {
                if (computers[cur][i] === 1 && check[i] === false) {
                    check[i] = true;
                    q.push(i);
                }
            }
        }
    }

    return answer;
}
