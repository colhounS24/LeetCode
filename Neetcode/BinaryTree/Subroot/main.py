# Surely the correct approach for this is to just do a dfs untils you find the node, and then do another dfs on that to make sure that the match?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

# 1. Traverse the original tree until you hit the subtree root
# 2. Traverse both trees simultaneously to see if they are the same
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def pre_order_dtf(node):
            if node is None:
                return "#"
            return(f"{str(node.val)},") + pre_order_dtf(node.left) + pre_order_dtf(node.right)
        
        big_string = pre_order_dtf(root)
        small_string = pre_order_dtf(subRoot)

        return small_string in big_string
            
            
            
        

        
    