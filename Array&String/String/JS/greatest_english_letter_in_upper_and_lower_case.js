/**
 * @param {string} s
 * @return {string}
 */
var greatestLetter = function(s) {
    for (let i = 25; i > -1; i--) {
        const up = String.fromCharCode(65 + i),
              low = String.fromCharCode(97 + i);
        if (s.includes(up) && s.includes(low)) return up;
    }
    return "";
};