from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict 
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sub_sum = defaultdict(TreeNode)
        res = defaultdict(int)
        def dfs(node): 
            # base case 
            if node == None: 
                return 0 
            if node.left == None and node.right == None:
                sub_sum[node] = node.val  
                return node.val 
            if node in sub_sum: 
                return sub_sum[node]
            total = node.val + dfs(node.left) + dfs(node.right)
            sub_sum[node] = total 
            return total 
        dfs(root) 
        for k, v in sub_sum.items(): 
            res[v] += 1 
        max_val = max(res.values()) 
        return [k for k, v in res.items() if v == max_val] 
        


