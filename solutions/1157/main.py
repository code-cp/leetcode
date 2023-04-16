from typing import * 

# 使用Boyer–Moore majority vote algorithm 注意freq diff相等时候的处理

class TreeNode:
    def __init__(self, start, end, val=0, freq_diff=0): 
        self.left = None  
        self.right = None  
        self.start = start  
        self.end = end 
        self.val = val 
        self.freq_diff = freq_diff

def queryRange(node, a, b): 
    if b < node.start or a > node.end: 
        return (0, 0)
    if a <= node.start and b >= node.end: 
        return (node.val, node.freq_diff)
    
    left = queryRange(node.left, a, b)
    right = queryRange(node.right, a, b)

    # No need to update, just return 
    if left[0] == right[0]: 
        return left[0], left[1] + right[1]
    else: 
        if left[1] > right[1]: 
            val = left[0]
        elif left[1] == right[1]: 
            # to avoid returning val as 0 
            val = max(left[0], right[0])
        else: 
            val = right[0]
        return val, abs(left[1] - right[1])

def lowerBound(arr, threshold): 
    # find first pos >= threshold 
    l, r = 0, len(arr)-1
    while l <= r: 
        mid = l+(r-l)//2
        if arr[mid] < threshold: 
            l = mid+1 
        else: 
            r = mid-1
    return l  

def upperBound(arr, threshold): 
    # find last pos <= threshold 
    l, r = 0, len(arr)-1
    while l <= r: 
        mid = l+(r-l)//2
        if arr[mid] <= threshold: 
            l = mid+1 
        else: 
            r = mid-1
    return r

class MajorityChecker:

    def __init__(self, arr: List[int]):
        n = len(arr)
        self.m = {}
        for i in range(n): 
            if self.m.get(arr[i], -1) == -1: 
                self.m[arr[i]] = []
            self.m[arr[i]].append(i)

        def initTree(node, a, b): 
            if a == b: 
                node.val = arr[a]
                node.freq_diff = 1 
                return 
            
            mid = a+(b-a)//2 
            if node.left is None: 
                node.left = TreeNode(a, mid)
                node.right = TreeNode(mid+1, b)
            
            initTree(node.left, a, mid)
            initTree(node.right, mid+1, b)
            
            if node.left.val == node.right.val: 
                node.val = node.left.val 
                node.freq_diff = node.left.freq_diff + node.right.freq_diff
            else:
                if node.left.freq_diff > node.right.freq_diff:  
                    node.val = node.left.val
                elif node.left.freq_diff == node.right.freq_diff:
                    # to avoid returning val as 0 
                    node.val = max(node.left.val, node.right.val)
                else:  
                    node.val = node.right.val 
                node.freq_diff = abs(node.left.freq_diff - node.right.freq_diff)
                
        self.root = TreeNode(0, n-1)
        initTree(self.root, 0, n-1)
        
    def query(self, left: int, right: int, threshold: int) -> int:
        val, freq_diff = queryRange(self.root, left, right)
        
        # double check whether val is valid 
        pos1 = lowerBound(self.m[val], left)
        pos2 = upperBound(self.m[val], right)
        
        count = pos2-pos1+1
        if count >= threshold: 
            return val 
        else: 
            return -1 
        
if __name__ == "__main__": 
    # arr = [1, 1, 2, 2, 1, 1]
    # mc = MajorityChecker(arr)
    # assert mc.query(0, 5, 4) == 1 
   
    arr = [2,2,1,2,1,2,2,1,1,2]
    mc = MajorityChecker(arr)
    # assert mc.query(2, 5, 4) == -1  
    # assert mc.query(0,5,6) == -1  
    # assert mc.query(0,1,2) == 2
    assert mc.query(2,3,2) == -1