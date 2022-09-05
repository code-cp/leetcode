# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import * 
class Solution:
    def dfs(self, node): 
        # Preorder (Root, Left, Right)
        # base case 
        if node.left is None and node.right is None: 
            code = hash(str(node.val))
            if code in self.subtrees and code not in self.res: 
                self.res[code] = node
            self.subtrees.add(code)
            return code
        if node.left: 
            code_left = self.dfs(node.left)
        else: 
            code_left = ""
        if node.right: 
            code_right = self.dfs(node.right)
        else: 
            code_right = ""
        code = hash(str(node.val) + "#" + str(code_left) + "*" + str(code_right))
        if code in self.subtrees and code not in self.res: 
            self.res[code] = node
        self.subtrees.add(code)
        return code
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.subtrees = set()
        self.res = {}
        self.dfs(root)
        return list(self.res.values())

if __name__ == "__main__": 
    s = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    assert s.findDuplicateSubtrees(root) == [root.right]