from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def countNodes(node):
            count = 0 
            if node is None: 
                return count  
            count += 1 
            count += countNodes(node.left)
            count += countNodes(node.right)
            return count 

        def findNode(node, target): 
            if node is None: 
                return None 
            if node.val == target: 
                return node 
            res = findNode(node.left, target)
            if res:
                return res 
            res = findNode(node.right, target)
            if res: 
                return res 
            return None 
        
        node = findNode(root, x)
        left_count = countNodes(node.left)
        right_count = countNodes(node.right)
        others_count = n - 1 - left_count - right_count 

        if left_count > n//2 or right_count > n//2 or others_count > n//2:
            return True 
        else: 
            return False 

if __name__ == "__main__": 
    s = Solution() 

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    n = 3 
    x = 2
    assert s.btreeGameWinningMove(root, n, x) 

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # n = 3 
    # x = 1
    # assert not s.btreeGameWinningMove(root, n, x) 