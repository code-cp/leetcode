# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(nodes, level):
            if level % 2 == 1:
                vals = [node.val for node in nodes]
                vals.reverse() 
                for val, node in zip(vals, nodes): 
                    node.val = val 
            new_nodes = []
            for node in nodes: 
                if node.left is None: 
                    return 
                new_nodes.append(node.left)
                new_nodes.append(node.right)
            bfs(new_nodes, level + 1)
            
        if root is None: 
            return None  
        bfs([root], 0)
        return root 

            