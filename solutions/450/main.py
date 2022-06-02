# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 

from collections import deque 
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def searchLeft(node):
            if node is None: 
                return None 
            if node.left is None:
                return node 
            else: 
                return searchLeft(node.left)  

        que = deque() 
        que.append((None, root)) 
        while que: 
            pre_node, node = que.popleft() 
            if node is None: 
                continue 
            if node.val == key: 
                leaf = searchLeft(node.right)
                if leaf is not None: 
                    leaf.left = node.left 
                else: 
                    node.right = node.left 
                if pre_node is None: 
                    return node.right
                elif pre_node.right and pre_node.right.val == node.val: 
                    pre_node.right = node.right 
                    return root
                elif pre_node.left and pre_node.left.val == node.val: 
                    pre_node.left = node.right
                    return root

            if node.val > key: 
                que.append((node, node.left))
            else: 
                que.append((node, node.right))

        return root 

