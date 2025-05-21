// Definition for a _Node.
function _Node(val, children) {
   this.val = val;
   this.children = children;
};

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    if (!root) return [];
    const stack = [root], ans = [];
    while (stack.length != 0) {
        const cur = stack.pop();
        if (cur) {
            stack.push(...cur.children.slice().reverse());
            // or
            // const n = cur.children.length;
            // for (let i = n-1; i >= 0; i--) {
            //     stack.push(cur.children[i]);
            // }
            ans.push(cur.val);
        }
    }
    return ans;
};
