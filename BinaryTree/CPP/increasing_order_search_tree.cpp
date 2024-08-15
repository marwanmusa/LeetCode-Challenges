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
    TreeNode* increasingBST(TreeNode* root) {
        vector<int> vals;
        inorder(root, vals);
        
        TreeNode* newRoot = new TreeNode(vals[0]);
        TreeNode* current = newRoot;

        for (int i = 1; i < vals.size(); i++) {
            current->right = new TreeNode(vals[i]);
            current = current->right;
        }

        return newRoot;
    }

    void inorder(TreeNode* root, vector<int>& vals) {
        if (root){
            inorder(root->left, vals);
            vals.push_back(root->val);
            inorder(root->right, vals);
        }
    }

    // What if we want to return the modified original root
    TreeNode* increasingBSTOptimized(TreeNode* root, TreeNode* tail = NULL) {
        if (!root) return tail;
        TreeNode* res = increasingBSTOptimized(root->left, root);
        root->left = nullptr;
        root->right = increasingBSTOptimized(root->right, tail);
        return res;
    }
};