from typing import * 

class TreeNode:
    def __init__(self, l, r, v):
        self.left = l
        self.right = r 
        self.val = v

class ChthollyTree:
    def __init__(self, start, end, val):
        self.nodes = []
        tr = TreeNode(start, end, val) 
        self.nodes.append(tr)

    def split(self, pos):
        n = len(self.nodes)
        left, right = 0, n-1
        while left <= right: 
            mid = (right - left)//2 + left 
            if self.nodes[mid].left < pos:
                left = mid + 1 
            elif self.nodes[mid].left > pos:
                right = mid - 1 
            else: 
                # no need to split if node.left == pos  
                return mid
        left -= 1 
        l, r, v = self.nodes[left].left, self.nodes[left].right, self.nodes[left].val 
        del self.nodes[left]
        tr = TreeNode(l, pos-1, v)  
        self.nodes.insert(left, tr)
        tr = TreeNode(pos, r, v)
        self.nodes.insert(left+1, tr)
        return left+1

class MyCalendarThree:

    def __init__(self):
        self.ct = ChthollyTree(0, 1e9, 0) 
        self.max_height = 0 

    def book(self, start: int, end: int) -> int:
        itl = self.ct.split(start)
        itr = self.ct.split(end)
        for i in range(itl, itr): 
            self.ct.nodes[i].val += 1
            self.max_height = max(self.max_height, self.ct.nodes[i].val) 
        return self.max_height 


if __name__ == "__main__": 
    obj = MyCalendarThree()
    start, end = 10, 20
    param_1 = obj.book(start,end)
    assert param_1 == 1 
    start, end = 50, 60
    param_2 = obj.book(start,end)
    assert param_2 == 1 
    start, end = 10, 40
    param_3 = obj.book(start,end)
    assert param_3 == 2
    start, end = 5, 15
    param_4 = obj.book(start,end)
    assert param_4 == 3 
    start, end = 5, 10
    param_5 = obj.book(start,end)
    assert param_5 == 3
    start, end = 25, 55
    param_6 = obj.book(start,end)
    assert param_6 == 3