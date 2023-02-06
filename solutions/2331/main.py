# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:  
        def evaluate(node):
            if node.left is None and node.right is None: 
                return True if node.val == 1 else False 
            if node.val == 2: 
                return evaluate(node.left) or evaluate(node.right)
            if node.val == 3: 
                return evaluate(node.left) and evaluate(node.right)
        return evaluate(root)