# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: 
            return None 
        tr = TreeNode(val)
        if root.val < val: 
            tr.left = root 
            root = tr 
            return root 
        node = root 
        while node: 
            if node.right is None:
                node.right = tr 
                return root 
            elif node.right.val < val: 
                temp = node.right 
                node.right = tr 
                # insert to left since all values in right subtree is left to new val
                tr.left = temp 
                return root 
            node = node.right
        return root   
                
            
            
