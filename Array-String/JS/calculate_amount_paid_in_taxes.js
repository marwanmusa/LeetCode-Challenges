/**
 * @param {number[][]} brackets
 * @param {number} income
 * @return {number}
 */
var calculateTax = function(brackets, income) {
    let ans = 0;
    let prev = 0;
    for (const bracket of brackets) {
        ans += Math.min(bracket[0] - prev, income) * (bracket[1] / 100.0);
        income -= (bracket[0] - prev);
        prev = bracket[0];
        if (income < 0) break;
    }
    return ans;
};
