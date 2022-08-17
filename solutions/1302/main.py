from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = 0 
        myque = deque()
        myque.append(root)
        while myque: 
            q_len = len(myque)
            res = 0 
            for i in range(q_len): 
                node = myque.popleft()
                res += node.val 
                if node.left:
                    myque.append(node.left)
                if node.right: 
                    myque.append(node.right)
        return res 
