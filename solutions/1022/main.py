from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 注意根节点是最高位，需要翻转路径
        path2sum = lambda x : sum(2**i * n for i, n in enumerate(x[::-1])) 
        que = deque() 
        que.append((root, [root.val])) 
        total = 0 
        while que: 
            node, path = que.popleft() 
            if node.left == None and node.right == None: 
                total += path2sum(path) 
                continue 
            if node.left: 
                que.append((node.left, path + [node.left.val])) 
            if node.right: 
                que.append((node.right, path + [node.right.val])) 
        return total 

