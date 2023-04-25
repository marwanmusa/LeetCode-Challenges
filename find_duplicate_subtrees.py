import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Task:
    Given the root of a binary tree, return all duplicate subtrees.

    For each kind of duplicate subtrees, you only need to return the root node of any one of them.

    Two trees are duplicate if they have the same structure with the same node values.
    """
    # Method 1 : A String Representation Approach
    def findDuplicateSubtrees(self, root):
        def traverse(node):
            if not node:
                return ""
            representation = ("(" + traverse(node.left) + ")" + str(node.val)
                              + "(" + traverse(node.right) + ")")
            cnt[representation] += 1
            if cnt[representation] == 2:
                res.append(node)
            return representation
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res


    # Method 2 : An Optimized Approach
    def findDuplicateSubtrees(self, root):
        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)
            return id
        triplet_to_id = dict()
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res