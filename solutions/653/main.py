from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, node, myset, k):
        if node is None: 
            return False 
        if k - node.val in myset:
            return True 
        myset.add(node.val)
        return self.traverse(node.left, myset, k) or self.traverse(node.right, myset, k)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        myset = set()
        return self.traverse(root, myset, k)

if __name__ == "__main__": 
    s = Solution()

    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node2, node4)

    node7 = TreeNode(7)
    node6 = TreeNode(6, None, node7)
    node5 = TreeNode(5, node3, node6)

    assert s.findTarget(node5, 9)
    assert not s.findTarget(node5, 28)