# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #recursive formula is 1 + left + right since root is good node
        def dfs(node, maxSeen):
            if not node:
                return 0

            good = node.val >= maxSeen
            
            return good + dfs(node.left, max(maxSeen, node.val)) + dfs(node.right, max(maxSeen, node.val))
            
        return dfs(root, float('-inf'))