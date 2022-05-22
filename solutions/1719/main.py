from typing import * 
from collections import defaultdict 

class TreeNode(): 
    def __init__(self, val=None):
        self.val = val 
        self.children = [] 

class Solution:
    def checkTree(self, node, depth, deg_dict): 
        total = 0 
        for c in node.children:
            c_total = self.checkTree(c, depth+1, deg_dict)
            if c_total == -1: 
                return -1 
            else: 
                total += c_total 
        degree = total + depth 
        if deg_dict[node.val] != degree:
            result = -1 
        else:  
            result = total+1 
        del deg_dict[node.val]
        return result

    def constructTree(self, deg_dict, adj_dict):
        tree_num = 1 
        nodes_dict = defaultdict(TreeNode)
        deg_list = list(deg_dict.keys())
        root = None 
        for idx, node in enumerate(deg_list): 
            if idx == len(deg_list)-1: 
                break 
            if node not in nodes_dict:
                c = TreeNode(node)
                nodes_dict[node] = c
            c = nodes_dict[node]
            for node_p in deg_list[idx+1:]:
                if node_p not in adj_dict[node]:
                    continue 
                if deg_dict[node_p] >= deg_dict[node]: 
                    if deg_dict[node_p] == deg_dict[node]:
                        tree_num = 2 
                    if node_p not in nodes_dict:
                        p = TreeNode(node_p)
                        nodes_dict[node_p] = p 
                    p = nodes_dict[node_p]
                    p.children.append(c)
                    root = p 
                    break 
        return (root, tree_num) 

    def checkWays(self, pairs: List[List[int]]) -> int:
        deg_dict = defaultdict(int)
        adj_dict = defaultdict(list)
        for p in pairs: 
            deg_dict[p[0]] += 1 
            deg_dict[p[1]] += 1
            adj_dict[p[0]].append(p[1])
            adj_dict[p[1]].append(p[0])
        deg_dict = dict(sorted(deg_dict.items(), key=lambda item: item[1]))
        root, tree_num = self.constructTree(deg_dict, adj_dict)
        if self.checkTree(root, 0, deg_dict) != -1 and len(deg_dict) == 0:
            return tree_num
        else: 
            return 0 

if __name__ == "__main__": 
    s = Solution()
    pairs = [[1,2],[2,3]]
    assert s.checkWays(pairs) == 1 
    pairs = [[1,2],[2,3],[1,3]]
    assert s.checkWays(pairs) == 2 
    pairs = [[1,2],[2,3],[2,4],[1,5]]
    assert s.checkWays(pairs) == 0
    pairs = [[1,5],[1,3],[2,3],[2,4],[3,5],[3,4]]
    assert s.checkWays(pairs) == 2 
    pairs = [[1,2],[2,3],[2,4],[1,5]]
    assert s.checkWays(pairs) == 0
    pairs = [[5,7],[11,12],[2,9],[8,10],[1,4],[3,6]]
    assert s.checkWays(pairs) == 0