/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
    let n = nums.length, cnt = 0, idx = 0;
    nums.sort((a, b) => a - b);
    while (cnt < n + 1) {
        if (idx > n - 1 || cnt > n - idx) return -1;
        if (cnt <= nums[idx] && cnt == n - idx) return cnt;
        else cnt > nums[idx] ? idx++ : cnt++;
    }
    return -1;
};

// Binary Search approach
/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
    nums.sort((a, b) => a - b);
    let r = nums.length, l = 0;
    while (l <= r) {
        let mid = l + Math.floor((r - l) / 2);
        let cnt = nums.filter(x => x >= mid).length;
        if (cnt === mid) return mid;
        else if (cnt > mid) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
};