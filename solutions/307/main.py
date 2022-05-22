from typing import * 

class TreeNode(object):
    def __init__(self, value = 0):
        self.value = value 
        self.left = None 
        self.right = None 

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.n = len(nums)
        if self.n == 0:
            return 
        
        self.seg_tree = self.construct_seg_tree(0, self.n - 1)

    def update(self, i: int, val: int):
        self.update_seg_tree(self.seg_tree, 0, self.n - 1, i, val)
        self.nums[i] = val 
        

    def sumRange(self, i: int, j: int):
        return self.tree_sum(self.seg_tree, 0, self.n-1, i, j)
    
    def construct_seg_tree(self, st, ed):
        tmp = TreeNode()
        mid = st + (ed - st) // 2 
        if st == ed:
            tmp.value = self.nums[st]
        else:
            tmp.left = self.construct_seg_tree(st, mid)
            tmp.right = self.construct_seg_tree(mid+1, ed)
            tmp.value = tmp.right.value + tmp.left.value 
        return tmp 

    def tree_sum(self, seg_tree, st, ed, i, j):
        if st >= i and ed <= j:
            return seg_tree.value 
        elif ed < i or st > j:
            return 0 
        else:
            mid = st + (ed - st) // 2 
        return self.tree_sum(seg_tree.left, st, mid, i, j) + \
            self.tree_sum(seg_tree.right, mid+1, ed, i, j)
        
    def update_seg_tree(self, seg_tree, st, ed, i, val):
        mid = st + (ed - st) // 2 
        diff = val - self.nums[i]
        if st == ed:
            seg_tree.value += diff 
        else:
            if i <= mid:
                seg_tree.value += diff 
                self.update_seg_tree(seg_tree.left, st, mid, i, val) 
            else:
                seg_tree.value += diff 
                self.update_seg_tree(seg_tree.right, mid+1, ed, i, val)
                
                
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)