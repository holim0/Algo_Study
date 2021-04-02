function solution(orders, course) {
    var answer = [];
    let obj = {};

    for (let i = 0; i < orders.length; i++) {
        let result = [];
        let arr = orders[i].split("");

        for (let j = 0; j < course.length; j++) {
            result.push(...getCombinations(arr, course[j]));
        }
        for (let j = 0; j < result.length; j++) {
            const cur = result[j].sort().join("");
            if (cur in obj) {
                obj[cur]++;
            } else {
                obj[cur] = 1;
            }
        }
    }

    const entries = Object.entries(obj);

    for (var i = 0; i < course.length; i++) {
        const curCnt = course[i];
        const possible = [];
        var maxOut = -1;
        for (var j = 0; j < entries.length; j++) {
            const key = entries[j][0];
            const value = entries[j][1];

            if (key.length == curCnt && value >= 2) {
                maxOut = Math.max(maxOut, value);
                possible.push([key, value]);
            }
        }

        for (var j = 0; j < possible.length; j++) {
            const key = possible[j][0];
            const value = possible[j][1];

            if (value == maxOut) {
                answer.push(key);
            }
        }
    }

    return answer.sort();
}

const getCombinations = function (arr, n) {
    const results = [];
    if (n === 1) return arr.map((e) => [e]);
    arr.forEach((e, idx, origin) => {
        const rest = origin.slice(idx + 1);
        const combinations = getCombinations(rest, n - 1);
        const attached = combinations.map((combination) => [e, ...combination]);
        results.push(...attached);
    });
    return results;
};
