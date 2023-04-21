from typing import * 
import math 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        memo = {}
        
        def minmax(node): 
            if node in memo: 
                return memo[node]
            if node is None: 
                return (float("inf"), -1)
            mi_l, ma_l = minmax(node.left)
            mi_r, ma_r = minmax(node.right)
            val = node.val 

            mi = min([mi_l, mi_r])
            ma = max([ma_l, ma_r])
            
            nonlocal ans
            if math.isfinite(mi):
                v = abs(val-mi)
                if v > ans:
                    ans = v
            if ma != -1:
                v = abs(val-ma)
                if v > ans:
                    ans = v
                                
            mi = min([mi_l, mi_r, val])
            ma = max([ma_l, ma_r, val])
            memo[node] = (mi, ma)
            return (mi, ma)
        
        minmax(root)
        
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    assert s.maxAncestorDiff(root) 
        

        
        