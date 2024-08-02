#include <vector>
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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> l, r;
        helper(root1, l);
        helper(root2, r);
        if (l.size() != r.size()) return false;
        for (int i = 0; i < l.size(); i++) {
            if (l[i] != r[i]) return false;
        }
        return true;
    }

    void helper(TreeNode* root, vector<int>& ans) {
        if (root->left != NULL) helper(root->left, ans);
        if (root != NULL && root->left == NULL && root->right == NULL) ans.push_back(root->val);
        if (root->right != NULL) helper(root->right, ans);
    }
};