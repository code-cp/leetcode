# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 1 
        max_val = root.val 
        
        def dfs(node, max_val):
            ans = 0  
            if node is None: 
                return ans 
            if node.val >= max_val:
                ans += 1 
                max_val = node.val 
            ans += dfs(node.left, max_val)
            ans += dfs(node.right, max_val)
            return ans 
        
        ans += dfs(root.left, max_val)
        ans += dfs(root.right, max_val) 
        
        return ans 
        