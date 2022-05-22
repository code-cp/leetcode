from typing import List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def robTree(self, node):
        result = [0, 0]
        if node is None: 
            return result
        left = self.robTree(node.left)
        right = self.robTree(node.right)
        # do not steal from current node 
        result[0] = max(left[0], left[1]) + max(right[0], right[1])
        # steal from current node 
        result[1] = node.val + left[0] + right[0]
        return result 
    def rob(self, root: TreeNode) -> int:
        result = self.robTree(root) 
        return max(result[0], result[1])

if __name__ == "__main__": 
    root = TreeNode(3)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1 
    root.right = node2 
    node3 = TreeNode(3)
    node1.right = node3
    node4 = TreeNode(1)
    node2.right = node4
    
    s = Solution()
    assert s.rob(root) == 7
