#include <vector>
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
    int sumRootToLeaf(TreeNode* root) {
        vector<int> res;
        unordered_map<TreeNode, vector<int>> umap = {{root, vector<int>(root->val)}};
        vector<unordered_map<TreeNode, vector<int>>> init{root, vector<int>(root->val)};
    }

    int conv(vector<int>& arr) {
        int res = 0;
        for (int i = 0, j = arr.size()-1; j >= 0 && i < arr.size(); j--, i++) {
            res += pow(2, i) + arr[j];
        }
        return res;
    }
};