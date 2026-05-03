# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursively check that height of left and right subtrees 
        # differs by no more than one

        def dfs(node):
            if not node:
                return True, 0
            
            lb, hl = dfs(node.left)
            rb, hr = dfs(node.right)

            balanced = lb and rb and abs(hl - hr) <= 1
            height = 1 + max(hl, hr)

            return balanced, height

        return dfs(root)[0]