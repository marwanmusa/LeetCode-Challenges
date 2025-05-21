/**
 * @param {number[]} arr
 * @param {number[][]} pieces
 * @return {boolean}
 */
var canFormArray = function(arr, pieces) {
    const idxs = {};
    const n = arr.length;
    for (let i = 0; i < n; i++) idxs[arr[i]] = i;

    let remain = n;
    for (const piece of pieces) {
        const piece_width = piece.length;
        if (idxs[piece[0]] == undefined) return false;

        let prev = idxs[piece[0]];
        remain--;

        for (let j = 1; j < piece_width; j++) {
            if (idxs[piece[j]] == undefined  || idxs[piece[j]] != ++prev)
                return false;
            remain--;
        }
    }

        return remain == 0;
};