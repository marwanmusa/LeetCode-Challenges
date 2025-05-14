/**
 * @param {number[]} releaseTimes
 * @param {string} keysPressed
 * @return {character}
 */
var slowestKey = function(releaseTimes, keysPressed) {
    const n = releaseTimes.length, durations = new Int32Array(n);
    let longest = releaseTimes[0], maxkey = keysPressed[0];
    durations[0] = releaseTimes[0];
    for (let i = 1; i < n; i++) {
        durations[i] = releaseTimes[i] - releaseTimes[i-1];
        if (longest < durations[i] || (longest == durations[i] && maxkey < keysPressed[i])) {
            longest = durations[i];
            maxkey = keysPressed[i];
        }
    }
    return maxkey;
};