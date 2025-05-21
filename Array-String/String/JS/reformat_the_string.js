/**
 * @param {string} s
 * @return {string}
 */
var reformat = function(s) {
    let digit = "", alpha = "", ans = "";

    for (const x of s) {
        (/^\d$/.test(x)) ? digit += x : alpha += x;
    }

    if (Math.abs(alpha.length - digit.length) > 1) return "";

    if (digit.length < alpha.length) {
        [digit, alpha] = [alpha, digit];
    }

    for (let i = 0; i < alpha.length; ++i) {
        ans += digit[i];
        ans += alpha[i];
    }

    if (digit.length > alpha.length) {
        ans += digit[digit.length - 1];
    }

    return ans;
};