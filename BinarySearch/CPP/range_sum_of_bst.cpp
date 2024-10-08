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
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (!root) return 0;
        else if (root->val < low) return rangeSumBST(root->right, low, high);
        else if (root->val > high) return rangeSumBST(root->left, low, high);
        return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }

    // shorter
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (!root) return 0;
        return (low <= root->val && root->val <= high? root->val : 0) + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }
};