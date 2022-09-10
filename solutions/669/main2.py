# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 

# 考虑binary search tree
class Solution:
    def dfs(self, node, l, h): 
        if node is None: 
            return None 
        if node.val < l: 
            return self.dfs(node.right, l, h)
        elif node.val > h: 
            return self.dfs(node.left, l, h)
        else: 
            if node.left: 
                node.left = self.dfs(node.left, l, h)
            if node.right: 
                node.right = self.dfs(node.right, l, h)
            return node 
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        root = self.dfs(root, low, high)
        return root 

if __name__ == "__main__":
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    assert s.trimBST(root, 1, 1)