# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #return max path sum without splitting
        def dfs(node):
            if not node:
                return (0, float("-inf"))
            
            l_up, l_best = dfs(node.left)
            r_up, r_best = dfs(node.right)

            # ignore negative paths for upward contribution
            l_up = max(0, l_up)
            r_up = max(0, r_up)

            # best path THROUGH this node (split allowed)
            split = node.val + l_up + r_up

            # best upward path (no split)
            up = node.val + max(l_up, r_up)

            # best path in entire subtree
            best = max(split, l_best, r_best)

            return (up, best)

        return dfs(root)[1]
            
