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
        que.append(root)
        max_width = 0
        continue_flag = True
        while que and continue_flag: 
            que_len = len(que)
            start, end = -1, -1 
            count = 0 
            continue_flag = False
            for i in range(que_len):
                node = que.popleft()
                count += 1

                if node and start == -1: 
                    start = count 
                if node: 
                    end = count 

                if node is None: 
                    que.append(None) 
                    que.append(None)  
                else: 
                    que.append(node.left)
                    que.append(node.right)
                    continue_flag = True 
            max_width = max(max_width, end - start + 1)
        return max_width

if __name__ == "__main__": 
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    assert s.widthOfBinaryTree(root) == 2 