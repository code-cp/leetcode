# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 是反转整个层，eg, 11112222 -> 22221111
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(left_node, right_node, level):
            if left_node is None or right_node is None: 
                return 
            if level % 2 == 1: 
                left_node.val, right_node.val = right_node.val, left_node.val
            dfs(left_node.left, left_node.right, level + 1)
            dfs(right_node.left, right_node.right, level + 1)
            
        if root is None: 
            return root  
        dfs(root.left, root.right, 1)
        return root 

            