from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None: 
            return res 
        mq = deque()
        mq.append(root)
        while mq: 
            sz = len(mq)
            mx = -float("inf") 
            for i in range(sz): 
                node = mq.popleft()
                mx = max(node.val, mx)
                if node.left: 
                    mq.append(node.left)
                if node.right: 
                    mq.append(node.right)
            res.append(mx)
        return res  

