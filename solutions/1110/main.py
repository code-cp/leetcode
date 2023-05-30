# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 
from collections import deque 

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        if root is None: 
            return ans 
        
        q = deque()
        q.append(root)
        if root.val not in to_delete: 
            # print(f"root {root.val}")
            ans.append(root)
        
        while len(q) > 0: 
            for _ in range(len(q)): 
                node = q.popleft()
                if node.left is not None: 
                    if node.left.val in to_delete: 
                        if node.left.left is not None: 
                            if node.left.left.val not in to_delete:
                                ans.append(node.left.left)
                            q.append(node.left.left)
                        if node.left.right is not None: 
                            if node.left.right.val not in to_delete:
                                ans.append(node.left.right)
                            q.append(node.left.right)
                        node.left = None 
                    else: 
                        q.append(node.left)
                        if node.val in to_delete: 
                            ans.append(node.left)
                if node.right is not None: 
                    if node.right.val in to_delete: 
                        if node.right.left is not None:
                            if node.right.left.val not in to_delete: 
                                ans.append(node.right.left)
                            q.append(node.right.left)
                        if node.right.right is not None: 
                            if node.right.right.val not in to_delete:
                                ans.append(node.right.right)
                            q.append(node.right.right)
                        node.right = None 
                    else: 
                        q.append(node.right) 
                        if node.val in to_delete: 
                            ans.append(node.right)               
        
        return ans 
                
        