/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    const town_judge = Array(n+1).fill(0);
    for (const [a, b] of trust) {
        town_judge[a]--;
        town_judge[b]++;
    }

    for (let i = 1; i < n+1; i++) {
        if (town_judge[i] == n - 1) return i;
    }

    return -1;
};