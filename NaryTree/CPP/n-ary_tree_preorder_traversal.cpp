#include <vector>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
public:
    vector<int> preorder(Node* root) {
        if (!root) return {};

        vector<Node*> stack;
        vector<int> ans;

        stack.push_back(root);
        while (stack.size() > 0) {
            Node* cur = stack.back();
            stack.pop_back();
            if (cur) {
                int n = cur->children.size();
                for (int i = n-1; i >= 0; i--) {
                    stack.push_back(cur->children[i]);
                }
                ans.push_back(cur->val);
            }
        }
        return ans;
    }

    // Recursive solution
    vector<int> preorder(Node* root) {
        if (!root) return {};
        vector<int> ans;
        ans.push_back(root->val);

        for (Node* child : root->children) {
            vector<int> childRes = preorder(child);
            ans.insert(ans.end(), childRes.begin(), childRes.end());
        }

        return ans;
    }
};