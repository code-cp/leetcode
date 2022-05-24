from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        que = deque([root])
        val = root.val 
        while que: 
            node = que.popleft()
            if node.val != val:
                return False 
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right) 
        return True 

