# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 

class Solution:
    def dfs(self, root):
        if root is None: 
            return 0 
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        left1 = left + 1 if root.left and root.left.val == root.val else 0
        right1 = right + 1 if root.right and root.right.val == root.val else 0
        # if cur node is root 
        self.max_count = max(self.max_count, left1 + right1)
        # else if cur node is not root 
        return max(left1, right1)

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 树形dp
        # dfs返回以当前结点为根结点(结尾)的最长同值路径
        self.max_count = 0 
        self.dfs(root)
        return self.max_count

if __name__ == "__main__": 
    s = Solution()

    # root = TreeNode(1)
    # root.left = TreeNode(1)
    # root.right = TreeNode(2)
    # assert s.longestUnivaluePath(root) == 1

    root = TreeNode(1)
    a1 = TreeNode(1)
    b1 = TreeNode(1)
    b2 = TreeNode(1)
    c1 = TreeNode(1)
    c2 = TreeNode(1)
    c3 = TreeNode(1)
    root.right = a1 
    a1.left = b1 
    a1.right = b2 
    b1.left = c1 
    b1.right = c2 
    b2.left = c3 
    assert s.longestUnivaluePath(root) == 4

