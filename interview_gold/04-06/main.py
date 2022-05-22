from typing import * 

# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
# 如果指定节点没有对应的“下一个”节点，则返回null。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque 
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        curNode = root 
        nextNode = None 
        stack = deque()
        while curNode != p:
            stack.append(curNode) 
            if p.val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right
        # curNode has subtree, search down 
        if curNode.right: 
            nextNode = curNode.right
            while nextNode.left:
                nextNode = nextNode.left
            return nextNode 
        # curNode does not have subtree, search up
        if len(stack) > 0: 
            preNode = stack.pop()
            while preNode: 
                if p.val > preNode.val: 
                    if len(stack) > 0: 
                        preNode = stack.pop()
                    else: 
                        return None 
                else:  
                    return preNode

if __name__ == "__main__": 
    s = Solution() 

    root = TreeNode(2)
    left = TreeNode(1) 
    right = TreeNode(3) 
    root.left = left 
    root.right = right 
    p = left 
    assert s.inorderSuccessor(root, p) == root 

    root = TreeNode(2)
    right = TreeNode(3) 
    root.right = right 
    p = root 
    assert s.inorderSuccessor(root, p) == right 

    root = TreeNode(0)
    p = root 
    assert s.inorderSuccessor(root, p) == None  

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)

    root.left.left.right = TreeNode(2)

    p = root.left.right
    assert s.inorderSuccessor(root, p) == root