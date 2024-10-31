#include <cmath>
#include <vector>
#include <utility>
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
    int sumRootToLeaf(TreeNode* root) {
        int res = 0;
        vector<pair<TreeNode*, vector<int>>> stk = {{root, {root->val}}};
        while (!stk.empty()) {
            TreeNode* node = stk.back().first;
            vector<int> path = stk.back().second;
            stk.pop_back();
            if (!node->left && !node->right) {
                res += conv(path);
            }
            if (node->right) {
                vector<int> rpath = path;
                rpath.push_back(node->right->val);
                stk.push_back({node->right, rpath});
            }
            if (node->left) {
                vector<int> lpath = path;
                lpath.push_back(node->left->val);
                stk.push_back({node->left, lpath});
            }
        }
        return res;
    }

    int conv(vector<int>& bitlist) {
        int res = 0;
        for (int bit : bitlist) res = (res << 1) | bit;
        return res;
    }
};
