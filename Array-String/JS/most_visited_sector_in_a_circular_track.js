/**
 * @param {number} n
 * @param {number[]} rounds
 * @return {number[]}
 */
var mostVisited = function(n, rounds) {
    const range = (start, end) => Array.from({ length: end - start + 1 }, (_, i) => start + i);
    const start = rounds[0], end = rounds[rounds.length - 1];
    if (start <= end) {
        return range(start, end);
    } else {
        return [...range(1, end), ...range(start, n)];
    }
};