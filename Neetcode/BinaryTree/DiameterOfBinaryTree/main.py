# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        def findDiameterDFS(root, diameter = 0):
            nonlocal max_diam
            if root is None:
                return 0
            
            lh =findDiameterDFS(root.left)
            rh = findDiameterDFS(root.right)
            max_diam = max(max_diam, (lh+rh))
            return 1+max(lh,rh)
        
        findDiameterDFS(root)
        return max_diam