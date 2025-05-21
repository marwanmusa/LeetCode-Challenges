/**
 * @param {string} s
 * @return {string}
 */
var modifyString = function(s) {
    const n = s.length;
    let res = "";
    if (n == 1 && s == "?") return "a";
    for (let i = 0; i < n; i++) {
        let cur = s[i];
        if (cur == '?') {
            for (let j = 97; j < 123; j++) {
                const m = res.length;
                const chrval = String.fromCharCode(j);
                if ((m > 0 && res[m-1] == chrval) || (i < n-1) && s[i+1] == chrval) continue;
                cur = chrval;
                break;
            }
        }
        res += cur;
    }
    return res;
};