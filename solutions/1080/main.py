from typing import * 

# ref https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/solutions/2278769/jian-ji-xie-fa-diao-yong-zi-shen-pythonj-64lf/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        limit -= root.val 
        if root.left is None and root.right is None: 
            # leaf node 
            # if limit > 0, means sum from root to leaf < limit, delete leaf 
            return None if limit > 0 else root 
        if root.left: 
            root.left = self.sufficientSubset(root.left, limit)
        if root.right: 
            root.right = self.sufficientSubset(root.right, limit)
        # if all children are deleted, then then delete node itself 
        if root.left is None and root.right is None: 
            return None
        # A node is insufficient if **every** root to leaf path intersecting this node has a sum strictly less than limit.
        # if a child is not deleted, then return root 
        return root 