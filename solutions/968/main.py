from typing import List 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:
    def __init__(self):
        self.result = 0

    def traversal(self, node: TreeNode) -> int:
        # base case
        if not node:
            return 2

        # post order traversal, left, right, visit
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # case 1, both children are covered
        if left == 2 and right == 2:
            return 0

        # case 2, one children is not covered
        if left == 0 or right == 0:
            self.result += 1
            return 1

        # case 3, both children has camera
        if left == 1 or right == 1:
            return 2

    def minCameraCover(self, root: TreeNode) -> int:
        # states:
        # 0 not covered
        # 1 has camera
        # 2 is covered

        if self.traversal(root) == 0:
            self.result += 1

        return self.result

if __name__ == "__main":
    root = TreeNode(0, None, None)
    middle = TreeNode(0, None, None)
    left = TreeNode(0, None, None)
    right = TreeNode(0, None, None)
    root.left = middle 
    middle.left = left 
    middle.right = right 

    s = Solution()
    assert s.minCameraCover(root) == 1
