from typing import List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseSum(self, node): 
        # base case 
        if node is None: 
            return 0 
        if node.left is None and node.right is None: 
            return node.val 
        
        # post order traversal 
        leftSum = self.traverseSum(node.left) 
        rightSum = self.traverseSum(node.right)
        node.val = leftSum + rightSum + node.val
        return node.val 

    def traverseTilt(self, root): 
        # base case 
        if root is None: 
            return 
        if root.left is None and root.right is None: 
            root.val = 0 
            return  

        # pre order traversal
        if root.left is None:  
            root.val = abs(root.right.val )
        elif root.right is None: 
            root.val = abs(root.left.val) 
        else: 
            root.val = abs(root.left.val - root.right.val)

        self.traverseTilt(root.left)
        self.traverseTilt(root.right)

    def findTilt(self, root: TreeNode) -> int:
        self.traverseSum(root) 
        self.traverseTilt(root)
        return self.traverseSum(root) 

if __name__ == "__main__": 
    root = TreeNode(-8)
    left = TreeNode(3)
    right = TreeNode(0)
    root.left = left 
    root.right = right 
    
    left1 = TreeNode(-8)
    left.left = left1 
    right1 = TreeNode(-1)
    left1.right = right1 
    right2 = TreeNode(8)
    right1.right = right2 
    
    s = Solution()
    result = s.findTilt(root)
    assert result == 18
