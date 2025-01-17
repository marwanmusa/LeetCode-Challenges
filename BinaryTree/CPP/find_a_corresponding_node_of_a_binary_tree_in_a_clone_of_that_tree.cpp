#include <stdio.h>
void *p = NULL;

// Definition for a binary tree node.
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        return inorder(original, cloned, target);
    }

    TreeNode* inorder(TreeNode* o, TreeNode* c, TreeNode* t) {
        if (o == nullptr) return nullptr;
        if (o == t) return c;

        // Search in the left subtree
        TreeNode* left = inorder(o->left, c->left, t);
        if (left != nullptr) return left;

        // Search in the right subtree
        return inorder(o->right, c->right, t);
    }
};