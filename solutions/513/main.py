from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node, level): 
        # base case 
        if node is None: 
            return 
        if node.left: 
            if level > self.max_level: 
                self.max_level = level 
                self.bottom_left = node.left.val 
            self.dfs(node.left, level+1)
        if node.right: 
            if level > self.max_level and node.left is None: 
                self.max_level = level 
                self.bottom_left = node.right.val 
            self.dfs(node.right, level+1)
        if node.left is None and node.right is None: 
            if level > self.max_level: 
                self.max_level = level 
                self.bottom_left = node.val 
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_level = -1  
        self.bottom_left = 0 
        self.dfs(root, 0)
        return self.bottom_left