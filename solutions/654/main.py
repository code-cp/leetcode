# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not isinstance(nums, list):
            nums = [nums]
        max_val = max(nums)
        max_idx = nums.index(max_val)
        root = TreeNode(max_val)
        if max_idx-1 >= 0:
            root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        if max_idx+1 < len(nums):
            root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return root 