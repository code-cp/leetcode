from typing import * 

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def traverse(root): 
    nodes = []
    queue = deque()
    queue.append(root) 
    while len(queue) > 0: 
        n = len(queue)
        for _ in range(n): 
            node = queue.popleft() 
            nodes.append([node.isLeaf, node.val]) 
            if node.topLeft: 
                queue.append(node.topLeft)
            if node.topRight: 
                queue.append(node.topRight)
            if node.bottomLeft: 
                queue.append(node.bottomLeft)
            if node.bottomRight: 
                queue.append(node.bottomRight)
    return nodes 

from collections import deque 
class Solution:
    @staticmethod
    def checkEqual(node):
        if node.topLeft is None or node.topRight is None or node.bottomLeft is None or node.bottomRight is None:
            return False 
        if node.topLeft.isLeaf == 0 or node.topRight.isLeaf == 0 or node.bottomLeft.isLeaf == 0 or node.bottomRight.isLeaf == 0:
            return False 
        return (node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val)

    def merge(self, qt1, qt2, node):
        # base case 
        if qt1 is None and qt2 is None: 
            return None 
        if qt1 is None or qt2 is None: 
            if qt1 is None: 
                return qt2 
            else: 
                return qt1 
        # if either is leaf and 1 
        if (qt1.isLeaf == 1 and qt1.val == 1) or (qt2.isLeaf == 1 and qt2.val == 1):
            node.isLeaf = 1 
            node.val = 1 
            return node 
        # if both are leaf and 0 
        if qt1.isLeaf == 1 and qt2.isLeaf == 1:
            node.val = 0 
            node.isLeaf = 1 
            return node 
        # if either is leaf, both are 0 
        if qt1.isLeaf == 1 or qt2.isLeaf == 1:
            if qt1.isLeaf:
                # NOTE, node is shallow copy, need to return instead of node = qt2
                return qt2 
            else:
                return qt1 
        # recurse when both are leaf 
        node.topLeft = Node(0, 0, None, None, None, None)
        node.topLeft = self.merge(qt1.topLeft, qt2.topLeft, node.topLeft)
        node.topRight = Node(0, 0, None, None, None, None)
        node.topRight = self.merge(qt1.topRight, qt2.topRight, node.topRight)
        node.bottomLeft = Node(0, 0, None, None, None, None)
        node.bottomLeft = self.merge(qt1.bottomLeft, qt2.bottomLeft, node.bottomLeft)
        node.bottomRight = Node(0, 0, None, None, None, None)
        node.bottomRight = self.merge(qt1.bottomRight, qt2.bottomRight, node.bottomRight)
        # check if can merge 
        if self.checkEqual(node):
            node.isLeaf = 1 
            node.val = node.topLeft.val
            node.topLeft = None 
            node.topRight = None
            node.bottomLeft = None
            node.bottomRight = None

        return node 

    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        root = Node(0, 0, None, None, None, None)
        root = self.merge(quadTree1, quadTree2, root) 
        # for debugging 
        # result = traverse(root)
        # print(result)
        return root 
