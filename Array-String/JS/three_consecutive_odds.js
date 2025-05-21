/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    let cnt = 0;
    for (x of arr) {
        cnt = x & 1? cnt+1 : 0;
        if (cnt == 3) return true;
    }
    return false;
};