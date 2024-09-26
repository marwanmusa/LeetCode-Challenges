#include <unordered_map>
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        unordered_map<int, int> height;
        unordered_map<int, int> parent;
        dfs(root, 0, 0, height, parent, x, y);
        return height[x] == height[y] && parent[x] != parent[y];
    }

    void dfs(TreeNode* root, int depth, int par, unordered_map<int, int>& height, unordered_map<int, int>& parent, int x, int y) {
        if (parent.size() == 2 && height.size() == 2) return;
        if (root) {
            if (root->val == x || root->val == y) {
                height[root->val] = depth;
                parent[root->val] = par;
            }
            dfs(root->left, depth+1, root->val, height, parent, x, y);
            dfs(root->right, depth+1, root->val, height, parent, x, y);
        }
    }
};