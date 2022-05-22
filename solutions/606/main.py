from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, node): 
        # base case 
        if node is None: 
            return ""

        # pre order 
        visit = str(node.val)
        # left node cannot be omitted 
        if node.left: 
            left = "(" + self.traverse(node.left) + ")"
        elif node.right: 
            left = "()"
        else: 
            left = ""
        # right node can be omitted 
        if node.right: 
            right = "(" + self.traverse(node.right) + ")"
        else: 
            right = ""
        result = visit + left + right
        return result

    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse(root)

if __name__ == "__main__": 
    s = Solution()

    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node1 = TreeNode(1)

    node2.left = node4 
    node1.left = node2 
    node1.right = node3 
    result = s.tree2str(node1)
    assert result == "1(2(4))(3)"
