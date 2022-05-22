from typing import List 

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        gQue = []
        gQue.append(node)
        visited = []
        visited.append(node)

        nodes_clone = {}

        while len(gQue) > 0:
            node_old = gQue[0]
            gQue.pop(0)
            if node_old.val not in nodes_clone:
                nodes_clone[node_old.val] = Node(node_old.val)
            node_new = nodes_clone[node_old.val]
            for n in node_old.neighbors:
                if n.val not in nodes_clone:
                    nodes_clone[n.val] = Node(n.val)
                n_clone = nodes_clone[n.val]
                node_new.neighbors.append(n_clone)
                if n not in visited:
                    gQue.append(n)
                    visited.append(n)

        return nodes_clone[node.val]

if __name__ == "__main__": 
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    s = Solution()
    node1_clone = s.cloneGraph(node1)
    for n in node1_clone.neighbors: 
        print(n.val)

