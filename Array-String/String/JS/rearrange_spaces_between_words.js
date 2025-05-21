/**
 * @param {string} text
 * @return {string}
 */
var reorderSpaces = function(text) {
    const spaces = (text.match(/ /g) || []).length,
          words = text.trim().split(/\s+/);
          n = words.length;
    if (n === 1) return words[0] + " ".repeat(spaces);
    const partition = Math.floor(spaces / (n - 1)),
          extras = spaces % (n - 1);
    let ans = "";
    ans += words.join(" ".repeat(partition));
    if (extras > 0) ans += " ".repeat(extras);
    return ans;
};