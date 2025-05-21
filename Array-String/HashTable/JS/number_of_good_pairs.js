/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    const cnt = {};
    nums.forEach(v => cnt[v] = (cnt[v] || 0) + 1);
    let res = 0;
    for (const [k, v] of Object.entries(cnt)) res += Math.floor(v * (v - 1) / 2);
    return res;
};