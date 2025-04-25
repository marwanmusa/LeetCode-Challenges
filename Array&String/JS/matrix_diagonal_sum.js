/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    const n = mat.length;
    let ans = 0;
    const odd = n & 1, mid = Math.floor(n / 2);
    for (let i = 0; i < n; i++) {
        if (odd && i == mid) ans += mat[i][i];
        else ans += mat[i][i] + mat[i][n-i-1];
    }
    return ans;
};