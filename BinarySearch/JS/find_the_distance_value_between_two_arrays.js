/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    arr2.sort((a, b) => a - b);
    let i = 0, j = 0, res = 0;
    const n = arr2.length;
    for (let x of arr1) {
        let l = 0, r = n-1;
        let hasclosevalue = false;
        while (l <= r) {
            const mid = Math.floor(l + (r - l) / 2), cur = arr2[mid];
            if (Math.abs(cur - x) <= d) {
                hasclosevalue = true;
                break;
            }
            else if (cur < x) l = mid + 1;
            else r = mid - 1;
        }
        if (!hasclosevalue) res++;
    }
    return res;
};