function solution(A) {
    var cntDict = {};
    var answer = [];
    var size = A.length;

    if (size === 0) {
        return -1;
    }

    for (const a of A) {
        if (a in cntDict) {
            cntDict[a] += 1;
        } else {
            cntDict[a] = 1;
        }
    }

    let sortobj = [];
    for (let number in cntDict) {
        sortobj.push([number, cntDict[number]]);
    }
    sortobj.sort(function (a, b) {
        return b[1] - a[1];
    });

    var maxVal = sortobj[0][1];
    if (maxVal <= size / 2) {
        return -1;
    }

    var target = Number(sortobj[0][0]);
    for (var i = 0; i < size; i++) {
        if (A[i] === target) {
            return i;
        }
    }
}
