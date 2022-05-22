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

from collections import deque 
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

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def quad_equal(node): 
            if node.topLeft is None or node.topRight is None or node.bottomLeft is None or node.bottomRight is None:
                return False 
            if node.topLeft.isLeaf == 0 or node.topRight.isLeaf == 0 or node.bottomLeft.isLeaf == 0 or node.bottomRight.isLeaf == 0:
                return False 
            if node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                return True 

        n = len(grid)
        root = Node(1, 0, None, None, None, None)

        # base case 
        if n == 1: 
            root.val = grid[0][0] 
            root.isLeaf = 1 
            return root 

        # recurse 
        root.topLeft = self.construct([row[0:n//2] for row in grid[0:n//2]]) 
        root.topRight = self.construct([row[n//2:] for row in grid[0:n//2]]) 
        root.bottomLeft = self.construct([row[0:n//2] for row in grid[n//2:]]) 
        root.bottomRight = self.construct([row[n//2:] for row in grid[n//2:]]) 

        if n % 2 == 0 and quad_equal(root): 
            root.val = root.topLeft.val 
            root.isLeaf = 1 
            root.topLeft = None 
            root.topRight = None
            root.bottomLeft = None
            root.bottomRight = None

        return root


if __name__ == "__main__":
    s = Solution() 

    grid = [[0,1],[1,0]]
    root = s.construct(grid) 
    result = traverse(root)
    assert result == [[0,1],[1,0],[1,1],[1,1],[1,0]]

    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    root = s.construct(grid) 
    result = traverse(root)
    assert result == [[0,1],[1,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1]]

    grid = [[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]]
    root = s.construct(grid) 
    result = traverse(root)
    assert result == [[0,1],[0,1],[0,1],[0,1],[0,1],[1,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1]]