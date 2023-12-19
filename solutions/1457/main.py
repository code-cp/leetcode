from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_ones(n): 
    res = 0 
    while n: 
        n &= (n-1)
        res += 1 
    return res 

class Solution:
    def dfs(self, node, path):
        # check if reach leaf  
        if node.left is None and node.right is None: 
            if count_ones(path) <= 1: 
                self.res += 1 
            return 
        # 1 <= Node.val <= 9 表示可以用状态压缩
        # 注意：只有在递归的时候才改变path的值
        if node.left is not None: 
            # record left node val 
            self.dfs(node.left, path ^ (1 << node.left.val))
        if node.right is not None: 
            # record right node val 
            self.dfs(node.right, path ^ (1 << node.right.val))
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        if root is None: 
            return self.res 
        self.dfs(root, 1 << root.val) 
        return self.res 
        