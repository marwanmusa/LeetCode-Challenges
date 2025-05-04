/**
 * @param {number[]} arr
 * @return {number}
 */
var sumOddLengthSubarrays = function(arr) {
    const n = arr.length;
    const prefixsum = new Array(n).fill(0);
    let ans = 0;
    prefixsum[0] = arr[0];
    for (let i = 1; i < n; i++) {
        prefixsum[i] = arr[i] + prefixsum[i-1];
    }

    const maxn = n % 2 == 0? n-1 : n;

    for (let i = 1; i <= maxn; i += 2) {
        for (let j = 0; j <= n - i; j++) {
            if (j === 0) {
                ans += prefixsum[i-1];
            } else {
                ans += prefixsum[j+i-1] - prefixsum[j-1];
            }
        }
    }
    return ans;
};

// o(n) time complexity
var sumOddLengthSubarrays = function(arr) {
    const n = arr.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const left = i + 1;
        const right = n - i;
        const total = left * right;
        const odd = Math.floor(total / 2);
        ans += arr[i] * (odd + (total % 2));
    }
    return ans;
}