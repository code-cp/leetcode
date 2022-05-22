from typing import List 
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # build graph
        nodes = []
        edges = []
        same_values = defaultdict(list)
        for i in range(len(arr)):
            nodes.append(i)
            edges.append([])
            if i-1 >= 0:
                edges[-1].append(i-1)
            if i+1 < len(arr):
                edges[-1].append(i+1)
            # treat adjacent nodes with same values as one node
            if i == 0 or i == len(arr)-1:
                same_values[arr[i]].append(i)
            elif i < len(arr)-1 and arr[i] != arr[i+1]:
                same_values[arr[i]].append(i)
            elif i > 0 and arr[i] != arr[i-1]:
                same_values[arr[i]].append(i)

        my_queue = []
        my_queue.append([nodes[0], 0])
        visited = set()
        visited.add(nodes[0])
        while len(my_queue) > 0:
            node = my_queue.pop(0)
            if node[0] == len(arr)-1:
                return node[1]
            dist = node[1] + 1

            if arr[node[0]] in same_values:
                neighbor_nodes = set(edges[node[0]] + same_values[arr[node[0]]])
                del same_values[arr[node[0]]]
            else:
                neighbor_nodes = edges[node[0]]

            for neighbor in neighbor_nodes:
                if neighbor == len(arr)-1:
                    return dist
                if neighbor in visited:
                    continue
                my_queue.append([neighbor, dist])
                visited.add(neighbor)

        return 0

if __name__ == "__main__":
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    s = Solution()
    assert s.minJumps(arr) == 3
