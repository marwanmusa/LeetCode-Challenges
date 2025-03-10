/**
 * @param {number[][]} grid
 * @return {number}
 */
var projectionArea = function(grid) {
    const len = grid.length;
    let top = 0, front = 0, rear = 0;
    const maxRear = new Array(len).fill(0);

    for (let i = 0; i < len; i++) {
        let maxFront = 0;
        for (let j = 0; j < len; j++) {
            if (grid[i][j] > 0) top++;
            maxFront = Math.max(maxFront, grid[i][j]);
            maxRear[j] = Math.max(maxRear[j], grid[i][j]);
        }
        front += maxFront;
    }

    rear = maxRear.reduce((sum, val) => sum + val, 0);
    return top + front + rear;
};