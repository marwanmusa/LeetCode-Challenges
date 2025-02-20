/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(l, h) {
    const nums = h - l + 1;
    const isOdd = nums & 1, lOdd = l & 1;
    const hn = Math.floor(nums / 2)
    if (isOdd && lOdd) return hn + 1;
    return hn
};