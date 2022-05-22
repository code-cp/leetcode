from typing import * 

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def dfs(self, result, node): 
        if node is None: 
            return 
        for c in node.children: 
            self.dfs(result, c)
        result.append(node.val)
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.dfs(result, root)
        return result 

if __name__ == "__main__": 
    s = Solution()

    node5 = Node(5, [])
    node6 = Node(6, [])
    node3 = Node(3, [node5, node6])
    node2 = Node(2, [])
    node4 = Node(4, [])
    node1 = Node(1, [node3, node2, node4])
    result = s.postorder(node1)
    assert result == [5,6,3,2,4,1]