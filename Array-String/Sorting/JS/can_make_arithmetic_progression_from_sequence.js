/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function(arr) {
    arr.sort((a, b) => a - b);
    let l1 = arr[0], l2 = arr[1], n = arr.length;
    let diff = l2 - l1;
    if (n == 2) return true;
    for (let i = 2; i < n; i++) {
        if (arr[i] - arr[i-1] != diff) return false;
    }
    return true;
};