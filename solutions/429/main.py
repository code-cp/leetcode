from typing import * 

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None:
            return res 
        que = [root]
        while len(que) > 0: 
            cur_res = []
            q_size = len(que)
            for _ in range(q_size): 
                node = que.pop(0)
                if node.children is not None: 
                    for child in node.children: 
                        que.append(child)
                cur_res.append(node.val) 
            res.append(cur_res)
        return res 

if __name__ == "__main__": 
    s = Solution() 

    node5 = Node(5) 
    node6 = Node(6) 
    node3 = Node(3, [node5, node6])
    node2 = Node(2) 
    node4 = Node(4)
    node1 = Node(1, [node3, node2, node4])
    
    assert s.levelOrder(node1) == [[1], [3, 2, 4], [5, 6]] 