/**
 * @param {number[]} nums
 * @return {number}
 */
var findShortestSubArray = function(nums) {
    const freq = new Map();
    const firstIdx = new Map();
    const lastIdx = new Map();

    for (let i = 0; i < nums.length; ++i) {
        const x = nums[i];
        freq.set(x, (freq.get(x) || 0) + 1);
        if (!firstIdx.has(x)) firstIdx.set(x, i);
        lastIdx.set(x, i);
    }

    let degree = 0, minLen = nums.length;

    for (const [num, count] of freq.entries()) {
        if (count > degree) {
            degree = count;
            minLen = lastIdx.get(num) - firstIdx.get(num) + 1;
        } else if (count == degree) {
            minLen = Math.min(minLen, lastIdx.get(num) - firstIdx.get(num) + 1);
        }
    }

    return minLen;
};