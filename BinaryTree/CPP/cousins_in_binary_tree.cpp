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
        dfs(root, 0, 0, height, parent);
        return height[x] == height[y] && parent[x] != parent[y];
    }

    void dfs(TreeNode* root, int depth, int par, unordered_map<int, int>& height, unordered_map<int, int>& parent) {
        if (root) {
            height[root->val] = depth;
            parent[root->val] = par;
            dfs(root->left, depth+1, root->val, height, parent);
            dfs(root->right, depth+1, root->val, height, parent);
        }
    }
};