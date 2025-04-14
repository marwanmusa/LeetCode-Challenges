/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    let ans = "";
    const n = s.length;
    for (let i = 0; i < n; i++) {
        const cur = s[i];
        if (ans.length > 0 && Math.abs(ans.at(-1).charCodeAt(0) - cur.charCodeAt(0)) == 32) {
            ans = ans.slice(0, -1);
            continue;
        }
        ans += cur;
    }
    return ans;
};