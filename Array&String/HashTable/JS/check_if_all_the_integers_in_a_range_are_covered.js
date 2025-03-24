/**
 * @param {number[][]} ranges
 * @param {number} left
 * @param {number} right
 * @return {boolean}
 */
var isCovered = function(ranges, left, right) {
    const covered = new Array(right - left + 1).fill(false);
    for (const [start, end] of ranges) {
        for (let i = Math.max(start, left); i <= Math.min(end, right); i++) {
            covered[i-left] = true;
        }
    }
    return covered.every(val => val === true);
};