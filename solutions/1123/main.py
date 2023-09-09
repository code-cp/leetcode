from typing import * 
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = {}
        q = deque()
        depth = 0 
        nodes[depth] = [(root, None)] 
        q.append(root)

        while len(q) > 0: 
            depth += 1 
            n = len(q)
            nodes[depth] = [] 
            for _ in range(n): 
                node = q.popleft()
                if node.left is not None: 
                    nodes[depth].append((node.left, node))
                    q.append(node.left)
                if node.right is not None: 
                    nodes[depth].append((node.right, node))
                    q.append(node.right)
        
        if len(nodes[depth]) == 0:
            depth -= 1 
        leafs = nodes[depth]
        while len(leafs) != 1:
            # if there is only one ancestor, return it 
            ancestors = set([node[1] for node in leafs])
            if len(ancestors) == 1:
                return ancestors.pop()
            # go up 
            depth -= 1 
            leafs = []
            for anc in ancestors: 
                for l in nodes[depth]: 
                    if l[0] == anc: 
                        leafs.append(l)

        # if there is only one node, return the node 
        return leafs[0][0]

if __name__ == '__main__': 
    s = Solution()
    
    root = TreeNode(1) 
    assert s.lcaDeepestLeaves(root) == root 

        
        