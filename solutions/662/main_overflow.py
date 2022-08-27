from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class Solution:
    def getHeight(self, node, height):
        if node is None:
            return height 
        height += 1 
        return max(self.getHeight(node.left, height), self.getHeight(node.right, height))
    def fillMat(self, res, height, node, row, col): 
        res[row][col] = str(node.val) 
        if node.left: 
            self.fillMat(res, height, node.left, row+1, col - 2**(height-row-1))
        if node.right: 
            self.fillMat(res, height, node.right, row+1, col + 2**(height-row-1))
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.getHeight(root, 0)
        height -= 1 
        n = 2 ** (height+1) - 1
        # python overflowerror cannot fit 'int' into an index-sized integer
        # n 590295810358705651711 height 69
        res = [[""] * n for _ in range(height+1)]
        self.fillMat(res, height, root, 0, (n-1)//2)
        return res 

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        tree_print = self.printTree(root)
        max_width = 0 
        for row in tree_print:
            start, end = -1, -1 
            for i in range(len(row)):
                if row[i] != "":
                    if start == -1:
                        start = i
                    end = i 
            max_width = max(max_width, end-start)
        return max_width

if __name__ == "__main__": 
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    assert s.widthOfBinaryTree(root) == 2 