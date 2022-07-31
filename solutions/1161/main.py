# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        myq = deque()
        myq.append(root)
        mymax = -float("inf")
        level = 1 
        res = level  
        while len(myq) > 0: 
            mylen = len(myq)
            total = 0 
            for i in range(mylen):
                node = myq.popleft() 
                total += node.val 
                if node.left is not None:
                    myq.append(node.left)
                if node.right is not None:
                    myq.append(node.right)
            if total > mymax:
                mymax = total 
                res = level 
            level += 1 
        return res 