# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 

# 考虑binary search tree，迭代
class Solution:
    def trimBST(self, root: Optional[TreeNode], l: int, h: int) -> Optional[TreeNode]:
        # 调整root
        while root and not (l <= root.val <= h): 
            if root.val < l: 
                root = root.right 
            elif root.val > l: 
                root = root.left 
        if root is None: 
            return None 
        # 调整左子树
        node = root 
        while node.left: 
            if node.left.val < l: 
                node.left = node.left.right 
            else: 
                node = node.left 
        # 调整右子树
        node = root 
        while node.right: 
            if node.right.val > h: 
                node.right = node.right.left 
            else: 
                node = node.right 
        return root 

if __name__ == "__main__":
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    assert s.trimBST(root, 1, 1)