# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # Create a datastructure with 4 parameters: (sum, isBST, maxLeft, minRight)
        ans = 0 

        def dfs(node):
            # NOTE, use nonlocal instead of global 
            nonlocal ans 
            # base case 
            if node is None: 
                return 0, True, -float("inf"), float("inf")
            elif node.left is None and node.right is None: 
                ans = max(ans, node.val)
                return node.val, True, node.val, node.val 
            
            # recursive  
            total_left, left_flag, mxl_left, mir_left = dfs(node.left)
            total_right, right_flag, mxl_right, mir_right = dfs(node.right)
            if not left_flag or not right_flag:
                return 0, False, float("inf"), -float("inf")
            if node.val <= mxl_left or node.val >= mir_right:
                return 0, False, float("inf"), -float("inf") 
            total = node.val + total_left + total_right 
            ans = max(ans, total)
            # if node appears on the left, find max. 
            mxl_left = max(node.val, mxl_right)
            # if node appears on the right, find min 
            mir_right = min(node.val, mir_left)
            return total, True, mxl_left, mir_right
        
        dfs(root)
        
        return ans 
                