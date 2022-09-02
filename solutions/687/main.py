# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 

from collections import deque 
class Solution:
    def dfs(self, node, count, first): 
        if node.left is None and node.right is None: 
            return count 
        elif node.left and node.right:
            if node.val == node.left.val == node.right.val:  
                if first:
                    return count + self.dfs(node.left, 1, False) + self.dfs(node.right, 1, False) 
                else: 
                    return max(self.dfs(node.left, count+1, False), self.dfs(node.right, count+1, False))
        if node.left: 
            if node.val == node.left.val: 
                return self.dfs(node.left, count+1, False)
        if node.right: 
            if node.val == node.right.val: 
                return self.dfs(node.right, count+1, False)
        return count 
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        que = deque()
        que.append(root)
        max_count = 0 
        while que: 
            q_len = len(que)
            for _ in range(q_len): 
                node = que.popleft()
                count = self.dfs(node, 1, True)
                max_count = max(count, max_count)
                if node.left:
                    que.append(node.left)
                if node.right: 
                    que.append(node.right)
        return max_count-1

if __name__ == "__main__": 
    s = Solution()

    # root = TreeNode(1)
    # root.left = TreeNode(1)
    # root.right = TreeNode(2)
    # assert s.longestUnivaluePath(root) == 1

    root = TreeNode(1)
    a1 = TreeNode(1)
    b1 = TreeNode(1)
    b2 = TreeNode(1)
    c1 = TreeNode(1)
    c2 = TreeNode(1)
    c3 = TreeNode(1)
    root.right = a1 
    a1.left = b1 
    a1.right = b2 
    b1.left = c1 
    b1.right = c2 
    b2.left = c3 
    assert s.longestUnivaluePath(root) == 4

