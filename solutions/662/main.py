from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque()
        que.append((root, 1))
        max_width = 0
        while que: 
            que_len = len(que)
            start, end = -1, -1 
            for i in range(que_len):
                node, idx = que.popleft()

                if node and start == -1: 
                    start = idx 
                if node:
                    end = idx 

                if node.left: 
                    que.append((node.left, 2*idx))
                if node.right: 
                    que.append((node.right, 2*idx+1))
            max_width = max(max_width, end - start + 1)
        return max_width

if __name__ == "__main__": 
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    assert s.widthOfBinaryTree(root) == 2 