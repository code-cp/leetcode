from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self): 
        self.node1 = None 
        self.node2 = None 
        self.pre = None 
    def traverse(self, node): 
        if node is None: 
            return 
        # left 
        self.traverse(node.left)
        # visit 
        if node.val < self.pre.val: 
            if self.node1 is None: 
                self.node1 = self.pre  
            elif self.node2 is None: 
                self.node2 = node 
        self.pre = node 
        # right 
        self.traverse(node.right)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = TreeNode(-float('inf'))  
        self.traverse(root)
        if self.node2 is None: 
            self.pre = TreeNode(-float('inf')) 
            self.traverse(root)
        temp = self.node1.val 
        self.node1.val = self.node2.val 
        self.node2.val = temp 

if __name__ == "__main__": 
    root = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(9)
    root.left = left 
    root.right = right 
    left1 = TreeNode(-2147483648)
    right1 = TreeNode(2)
    left.left = left1 
    left.right = right1
    s = Solution()
    s.recoverTree(root)
    assert root.left.val == 2
