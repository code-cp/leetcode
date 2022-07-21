from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def checkValid(self, root): 
        # base case 
        if root is None: 
            return False   
        # recurse, post order traversal LRV
        if not self.checkValid(root.left) and not self.checkValid(root.right): 
            return root.val == 1 
        return True 
    def buildTree(self, root): 
        res = None 
        if self.checkValid(root):
            res = TreeNode(root.val)
            res.left = self.buildTree(root.left)
            res.right = self.buildTree(root.right)
        return res 
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.buildTree(root)
        return res 


if __name__ == "__main__": 
    s = Solution()

    # root = TreeNode(1)
    # node1 = TreeNode(0)
    # node2 = TreeNode(0)
    # node3 = TreeNode(1)
    # root.right = node1 
    # node1.left = node2 
    # node1.right = node3 
    # s.pruneTree(root)

    root = TreeNode(1)
    node1 = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(1)
    node4 = TreeNode(1)
    node5 = TreeNode(0)
    node6 = TreeNode(1)
    node7 = TreeNode(0)

    root.left = node1 
    root.right = node2 
    node1.left = node3
    node1.right = node4 
    node2.left = node5
    node2.right = node6 
    node3.left = node7
    s.pruneTree(root)
    