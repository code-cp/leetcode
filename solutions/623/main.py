# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: 
            node = TreeNode(val)
            node.left = root 
            return node 

        level = 1 
        myque = deque()
        myque.append(root)
        while myque:
            total = len(myque)
            if level == depth-1: 
                for i in range(total): 
                    node = myque.popleft()
                    temp_left = node.left 
                    temp_right = node.right 
                    tr_left = TreeNode(val)
                    tr_right = TreeNode(val)
                    node.left = tr_left
                    tr_left.left = temp_left 
                    node.right = tr_right
                    tr_right.right = temp_right 
                break 


            for i in range(total): 
                node = myque.popleft()
                if node.left:
                    myque.append(node.left)
                if node.right: 
                    myque.append(node.right)
            level += 1 
        return root 
