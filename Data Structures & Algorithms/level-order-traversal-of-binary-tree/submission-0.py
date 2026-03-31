# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        d = deque([(root, 0)])

        while d:
            node, level = d.popleft()
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            
            if node.left:
                d.append((node.left, level + 1))
            if node.right:
                d.append((node.right, level + 1))
        return res
            
