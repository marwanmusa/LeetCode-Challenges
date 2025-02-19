/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */

var findKthPositive = function(arr, k) {
    let l = 0, r = arr.length;
    while (l < r) {
        let m = Math.floor((l + r) / 2);
        if (arr[m] - m - 1 < k) l = m + 1;
        else r = m;
    }
    return l + k;
};

console.log(findKthPositive([2,3,4,7,11], 5)); // Output: 9
console.log(findKthPositive([1,2,3,4], 2)); // Output: 6