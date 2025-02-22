/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    let cnt = 0, n = arr.length;
    for (let i = 0; i < n - 2; i++) {
        for (let j = i + 1; j < n - 1; j++) {
            let a_ = Math.abs(arr[i] - arr[j]);
            if (a < a_) continue;
            for (let k = j + 1; k < n; k++) {
                let b_ = Math.abs(arr[j] - arr[k]), c_ = Math.abs(arr[i] - arr[k]);
                if (b < b_ || c < c_) continue;
                if (a_ <= a && b_ <= b && c_ <= c) cnt++;
            }
        }
    }
    return cnt;
};