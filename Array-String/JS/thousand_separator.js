/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function(n) {
    let s = n.toString(), ans = "";
    const le = s.length;
    for (let i = 0; i < le; i++) {
        if (i > 0 && (le - i) % 3 == 0) ans += ".";
        ans += s[i];
    }
    return ans;
};