#include <set>
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
    bool isUnivalTree(TreeNode* root) {
        set<int> values;
        helper(root, values);
        return values.size() == 1;
    }

    void helper(TreeNode* root, set<int>& values) {
        if (root) {
            values.insert(root->val);
            helper(root->right, values);
            helper(root->left, values);
        }
    }

    // shorter
    bool isUnivalTree(TreeNode* root, int val = -1) {
        if (!root) return true;
        if (val < 0) val = root-> val;
        return root->val == val && isUnivalTree(root->left, val) && isUnivalTree(root->right, val);
    }

    // one-liner
    // bool isUnivalTree(TreeNode* root) {
    //     return (!root->left || root->left->val == root->val && isUnivalTree(root->left)) &&
    //            (!root->right || root->right->val == root->val && isUnivalTree(root->right));
    // }
};