/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    if (n === 0) return 0;
    const dp = Array(n + 1).fill(0);
    dp[0] = 0;
    dp[1] = 1;
    for (let i = 0; i < n + 1; i++) {
        if (i % 2 == 0) dp[i] = dp[Math.floor(i / 2)];
        else dp[i] = dp[Math.floor(i / 2)] + dp[Math.floor(i / 2) + 1];
    }
    return Math.max(...dp);
};