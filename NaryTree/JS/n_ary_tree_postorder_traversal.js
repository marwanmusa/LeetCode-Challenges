/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var postorder = function(root) {
    if (!root) return [];
    let ans = [];
    for (const child of root.children) {
        const cur = postorder(child);
        ans.push(...cur);
    }
    ans.push(root.val);
    return ans;
};

//iterative
var postorder = function(root) {
    if (!root) return [];
    let ans = [];
    let stack = [root];
    while (stack.length) {
        const cur = stack.pop();
        ans.push(cur.val);
        stack.push(...cur.children);
    }
    return ans.reverse();
};