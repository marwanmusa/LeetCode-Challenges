#include <vector>
#include <stack>
#include <algorithm>

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
    vector<int> postorder(Node* root) {
        if (!root) return {};
        vector<int> ans;
        for (Node* child : root->children) {
            vector<int> cur = postorder(child);
            ans.insert(ans.end(), cur.begin(), cur.end());
        }
        ans.push_back(root->val);
        return ans;
    }

    //iterative
    vector<int> postorder(Node* root) {
        if (!root) return {};
        vector<int> ans;
        stack<Node*> st;
        st.push(root);
        while (!st.empty()) {
            Node* cur = st.top();
            st.pop();
            ans.push_back(cur->val);
            for (Node* child : cur->children) {
                st.push(child);
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};