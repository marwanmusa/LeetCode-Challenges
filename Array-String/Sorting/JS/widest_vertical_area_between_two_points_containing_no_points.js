/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {
    points.sort((a, b) => a[0] - b[0]);
    const n = points.length;
    let res = 0;
    for (let i = 1; i < n; i++) {
        res = Math.max(res, points[i][0] - points[i-1][0]);
    }
    return res;
};