from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def traverse(node): 
            # in order 
            nonlocal nodes 
            if node is None: 
                return 
            traverse(node.left)
            nodes.append(node.val)
            traverse(node.right)
        traverse(root)
        return nodes[k-1]
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.kthSmallest()