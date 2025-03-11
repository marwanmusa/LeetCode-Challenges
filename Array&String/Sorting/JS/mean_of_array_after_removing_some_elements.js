/**
 * @param {number[]} arr
 * @return {number}
 */
var trimMean = function(arr) {
    arr.sort(function(a, b){return a - b});
    const n = arr.length;
    const cut = n / 20;
    const sum = arr.slice(cut, -cut).reduce((partSum, a) => partSum + a, 0);
    return sum / (n - (2 * cut));
};