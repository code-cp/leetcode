from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        q = deque()
        q.append(root)
        while len(q) > 0: 
            q_size = len(q)
            total = 0 
            for _ in range(q_size): 
                node = q.popleft()
                if node is None: 
                    continue 
                total += node.val 
                q.append(node.left)
                q.append(node.right)
            # NOTE, do NOT add level with all None 
            if total != 0:
                level_sums.append(total)
        level_sums.sort(reverse=True)
        return level_sums[k-1] if len(level_sums) >= k else -1 

if __name__ == "__main__": 
    s = Solution() 

    root = TreeNode(5)
    left1 = TreeNode(8)
    right1 = TreeNode(9)
    root.left = left1 
    root.right = right1 
    left21 = TreeNode(2)
    right22 = TreeNode(1)
    root.left.left = left21 
    root.left.right = right22 
    left23 = TreeNode(3)
    right24 = TreeNode(7)
    root.right.left = left23
    root.right.right = right24 
    k = 4
    assert s.kthLargestLevelSum(root, k) == -1 
