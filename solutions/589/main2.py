from typing import List 

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque  

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None: 
            return result 
        que = deque()
        que.append(root)
        while len(que) > 0: 
            node = que.pop()
            result.append(node.val)
            for c in node.children[::-1]: 
                que.append(c)
        return result

if __name__ == "__main__": 
    s = Solution()

    node4 = Node(4, [])
    node2 = Node(2, [])
    node5 = Node(5, [])
    node6 = Node(6, [])
    node3 = Node(3, [node5, node6])
    root = Node(1, [node3, node2, node4])
    result = s.preorder(root)
    assert result == [1,3,5,6,2,4]