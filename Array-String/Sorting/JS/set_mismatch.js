/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    nums.sort((a, b) => a - b);
    let duplicate = -1, missing = -1, i = 1, prev = -1;
    for (const num of nums) {
        if (prev == num) {
            duplicate = num;
        }
        prev = num;
        if (i == num) i++;
    }
    return [duplicate, i];
};

// O(1) space solution without sorting
var findErrorNums = function(nums) {
    let duplicate = -1, missing = -1;

    for (const num of nums) {
        const index = Math.abs(num) - 1;
        if (nums[index] < 0) {
            duplicate = Math.abs(num);
        } else {
            nums[index] *= -1;
        }
    }

    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] > 0) {
            missing = i + 1;
            break;
        }
    }

    return [duplicate, missing];
};