class TreeNode:
    def __init__(self, l, r, v):
        self.left = l
        self.right = r 
        self.val = v

class ChthollyTree:
    def __init__(self, ):
        self.nodes = []

    def bsearch(self, pos):
        n = len(self.nodes)
        left, right = 0, n-1
        while left <= right: 
            mid = (right - left)//2 + left 
            if self.nodes[mid].left < pos:
                left = mid + 1 
            elif self.nodes[mid].left > pos:
                right = mid - 1 
            else: 
                return mid, False 
        return left, True 

    def split(self, pos):
        left, flag = self.bsearch(pos)
        if not flag: 
            return left
        left -= 1 
        l, r, v = self.nodes[left].left, self.nodes[left].right, self.nodes[left].val 
        del self.nodes[left]
        tr = TreeNode(l, pos-1, v)  
        self.nodes.insert(left, tr)
        tr = TreeNode(pos, r, v)
        self.nodes.insert(left+1, tr)
        return left+1

    def assign(self, l, r, v): 
        if len(self.nodes) == 0: 
            tr = TreeNode(l, r, v) 
            self.nodes.append(tr)
            return 
        itr = self.split(r+1)
        itl = self.split(l) 
        del self.nodes[itl:itr]
        tr = TreeNode(l, r, v) 
        self.nodes.insert(itl, tr) 

class RangeModule:

    def __init__(self):
        self.ct = ChthollyTree() 
        self.ct.assign(1, 1e9, 0) 

    def addRange(self, left: int, right: int) -> None:
        itr = self.ct.split(right)
        itl = self.ct.split(left)
        self.ct.assign(left, right-1, 1) 

    def queryRange(self, left: int, right: int) -> bool:
        right -= 1 
        itr, _ = self.ct.bsearch(right) 
        if itr >= len(self.ct.nodes): 
            return False 
        if self.ct.nodes[itr].left > right: 
            itr = max(itr-1, 0)  
        itl, _ = self.ct.bsearch(left) 
        if self.ct.nodes[itl].left > left: 
            itl = max(itl-1, 0)    
        if self.ct.nodes[itl].left > left or self.ct.nodes[itr].right < right: 
            return False
        for i in range(itl, itr+1): 
            if self.ct.nodes[i].val == 0: 
                return False 
            if i != itl and self.ct.nodes[i].left-1 > self.ct.nodes[i-1].right: 
                return False 
        return True 

    def removeRange(self, left: int, right: int) -> None:
        itr = self.ct.split(right)
        itl = self.ct.split(left)
        self.ct.assign(left, right-1, 0) 

if __name__ == "__main__": 
    obj = RangeModule()
    obj.removeRange(8, 9)
    obj.addRange(6, 10)
    assert not obj.queryRange(4, 7)
    obj.addRange(3, 4)
    obj.addRange(1, 5)
    obj.addRange(3, 6)
    assert obj.queryRange(2, 4)
    assert obj.queryRange(7, 8)
    assert obj.queryRange(1, 4)
    obj.addRange(4, 5)
    assert obj.queryRange(7, 8)
    obj.removeRange(8, 9)
    assert obj.queryRange(1, 7)

    obj = RangeModule()
    left, right = [10, 20]
    obj.addRange(left,right)
    left, right = [14, 16]
    obj.removeRange(left,right)
    left, right = [10, 14]
    assert obj.queryRange(left, right)
    left, right = [13, 15]
    assert not obj.queryRange(left, right)
    left, right = [16, 17]
    assert obj.queryRange(left, right)

    obj = RangeModule()
    left, right = [10, 180]
    obj.addRange(left,right)
    # [10-180)
    left, right = [150, 200]
    obj.addRange(left,right)
    # [10-200)
    left, right = [250,500]
    obj.addRange(left,right)
    # [10-200) [250-500)
    left, right = [50,100]
    assert obj.queryRange(left, right)
    # [10-200) [250-500)
    left, right = [180,300]
    assert not obj.queryRange(left, right)
    # [10-200) [250-500)
    left, right = [600,1000]
    assert not obj.queryRange(left, right)
    left, right = [50,150]
    obj.removeRange(left, right)
    # [10-50) [150-200) [250-500)
    left, right = [50,100]
    assert not obj.queryRange(left, right)