/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function(words) {
    let n = words.length;
    const res = [];
    let prev = "";

    for (const s of words) {
        const cur = s.split('').sort().join('');
        if (prev != cur) {
            res.push(s);
            prev = cur;
        }
    }
    return res;
};