from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(nodeA, nodeB):
            if nodeA is None and nodeB is not None:
                return False
            elif nodeA is not None and nodeB is None:
                return False
            elif nodeA is None and nodeB is None:
                return True
    
            if nodeA.val != nodeB.val:
                return False
            
            return dfs(nodeA.left, nodeB.left) and dfs(nodeA.right, nodeB.right)
                
        return dfs(p,q)