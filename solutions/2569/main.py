from typing import * 

class segmentTreeNode: 
    # info is the sum of range 
    # lazy tag means if the child ranges are pending propagation 
    # lazy val means how many flips need to propagate to child 
    def __init__(self, a, b, val):
        self.lazy_tag = 0 
        self.lazy_val = 0 
        self.start, self.end = a, b 
        self.left, self.right = None, None 
        
        if isinstance(val, list): 
            self.newArr(a, b, val)
        else: 
            self.newNum(a, b, val) 
        
    def newNum(self, a, b, num): 
        if a == b: 
            self.info = num 
            return 
        
        mid = (b-a)//2 + a 
        if self.left is None: 
            self.left = segmentTreeNode(a, mid, num)
            self.right = segmentTreeNode(mid+1, b, num)
            self.info = self.left.info + self.right.info 
        
    def newArr(self, a, b, arr): 
        if a == b: 
            self.info = arr[a]
            return 
        
        mid = (b-a)//2+a 
        if self.left is None:
            self.left = segmentTreeNode(a, mid, arr)
            self.right = segmentTreeNode(mid+1, b, arr)
            self.info = self.left.info + self.right.info 

    def queryRange(self, a, b): 
        if b < self.start or a > self.end: 
            return 0 
        
        if a <= self.start and b >= self.end: 
            return self.info 
        
        if self.left is not None: 
            self.pushDown()
            res = self.left.queryRange(a, b) + self.right.queryRange(a, b) 
            info = self.left.info + self.right.info 
            return res 
        
        # should not reach here 
        raise NotImplementedError("not implemented.") 

    def pushDown(self): 
        # push down的更新过程，就是更新左右子树的lazy tag, lazy val, info 
        # 注意这个函数不需要递归
        if self.lazy_tag == 1 and self.left is not None: 
            # only need to flip when lazy val is odd 
            if self.lazy_val % 2 == 1: 
                # flip 0 and 1 
                self.left.info = (self.left.end - self.left.start + 1) - self.left.info 
                self.right.info = (self.right.end - self.right.start + 1) - self.right.info 
                
                # if current range is updated, then need to propagate to child 
                self.left.lazy_tag = 1 
                self.left.lazy_val += self.lazy_val 
                self.right.lazy_tag = 1 
                self.right.lazy_val += self.lazy_val 
                
                # current range is processed 
                self.lazy_tag = 0 
                self.lazy_val = 0 
                
    def updateRange(self, a, b): 
        if b < self.start or a > self.end: 
            return 
       
        # 如果更新区间完全包含当前区间，那只需要把当前区间更新，标记lazy tag，然后返回 
        # 注意，只有当前区间完全在更新区间范围内，才更新
        if a <= self.start and b >= self.end: 
            self.info = (self.end - self.start + 1) - self.info 
            self.lazy_tag = 1 
            self.lazy_val += 1
            return 
        
        # 如果更新区间跟当前区间有交集,则需要先向下传递lazy tag,然后分别更新左右子区间
        if self.left is not None: 
            self.pushDown()
            self.left.updateRange(a, b) 
            self.right.updateRange(a, b) 
            self.info = self.left.info + self.right.info 

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        root = segmentTreeNode(0, n-1, nums1)
        
        res = []
        total2 = sum(nums2)
        
        for q in queries: 
            if q[0] == 1: 
                root.updateRange(q[1], q[2])
            elif q[0] == 2: 
                total2 += root.queryRange(0, n-1) * q[1]
            else: 
                res.append(total2)   
                
        return res      