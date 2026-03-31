# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        #return max path sum without splitting
        def dfs(root):
            if not root:
                return 0
            
            lmax = dfs(root.left)
            rmax = dfs(root.right)
            #check negatives
            lmax = max(0, lmax)
            rmax = max(0, rmax)

            #compute max path sum with split
            res[0] = max(res[0], root.val + lmax + rmax)

            #return value without splitting
            return root.val + max(lmax, rmax)
        dfs(root)
        return res[0]
            
