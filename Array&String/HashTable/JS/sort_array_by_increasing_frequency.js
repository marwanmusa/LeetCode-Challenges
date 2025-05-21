/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
    const freqs = {}, freqToNums = {}, ans = [];
    for (const x of nums) freqs[x] = (freqs[x] || 0) + 1;;
    for (const [n, freq] of Object.entries(freqs)) {
        if (!freqToNums[freq])  freqToNums[freq] = [];
        freqToNums[freq].push(Number(n));
    }
    for (const f of Object.keys(freqToNums).sort((a, b) => a - b)) {
        const numsAtFreq = freqToNums[f];
        numsAtFreq.sort((a, b) => b - a);
        for (const num of numsAtFreq) {
            ans.push(...Array(Number(f)).fill(Number(num)));
        }
    }
    return ans;
};


// sort nums using custom comparator
var frequencySort = function(nums) {
    const freq = {};

    // Step 1: Count frequencies
    for (const num of nums) {
        freq[num] = (freq[num] || 0) + 1;
    }

    // Step 2: Sort with custom comparator
    nums.sort((a, b) => {
        const fa = freq[a], fb = freq[b];
        if (fa !== fb) return fa - fb;      // Increasing frequency
        return b - a;                        // Descending value if freq same
    });

    return nums;
};
