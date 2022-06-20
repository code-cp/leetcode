# wrong 
class RangeModule:

    def __init__(self):
        self.intervals = []

    def bsearch(self, target): 
        if len(self.intervals) == 0: 
            return 0 
        l, r = 0, len(self.intervals)-1
        while l <= r: 
            mid = (r-l)//2 + l 
            if self.intervals[mid][0] < target:
                l = mid + 1 
            elif self.intervals[mid][0] >= target:
                r = mid - 1 
        return l-1

    def addRange(self, left: int, right: int) -> None:
        if len(self.intervals) == 0:
            self.intervals.insert(0, [left, right]) 
            return 
        l = self.bsearch(left)
        r = self.bsearch(right)
        if self.intervals[r][1] < left or self.intervals[l][0] > right: 
            self.intervals.insert(l+1, [left, right]) 
            return 
        if r+1 < len(self.intervals) and self.intervals[r+1][0] == right: 
            r += 1 
        new_left = min(left, self.intervals[l][0])
        new_right = max(right, self.intervals[r][1])
        if left <= new_left and right >= new_right: 
            del self.intervals[max(l, 0):r+1] 
        self.intervals.insert(l+1, [new_left, new_right]) 

    def queryRange(self, left: int, right: int) -> bool:
        r = self.bsearch(right)
        return self.intervals[r][0] <= left and self.intervals[r][1] >= right 

    def removeRange(self, left: int, right: int) -> None:
        l = self.bsearch(left)
        r = self.bsearch(right)

        if self.intervals[r][1] <= left: 
            return 
        if self.intervals[l][0] >= right: 
            return 

        left1 = self.intervals[l][0] 
        right1 = left
        left2 = right
        right2 = max(right, self.intervals[r][1])

        del self.intervals[l:r+1]
        
        if right1 > left1: 
            self.addRange(left1, right1) 
        if right2 > left2: 
            self.addRange(left2, right2) 

if __name__ == "__main__": 
    # obj = RangeModule()
    # left, right = [10, 20]
    # obj.addRange(left,right)
    # left, right = [14, 16]
    # obj.removeRange(left,right)
    # left, right = [10, 14]
    # assert obj.queryRange(left, right)
    # left, right = [13, 15]
    # assert not obj.queryRange(left, right)
    # left, right = [16, 17]
    # assert obj.queryRange(left, right)




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


    # obj = RangeModule()
    # left, right = [6, 8]
    # obj.addRange(left,right)
    # # [6-8)
    # left, right = [7, 8]
    # obj.removeRange(left, right)
    # # [6-7)
    # left, right = [8, 9]
    # obj.removeRange(left, right)
    # # [6-7)
    # left, right = [8, 9]
    # obj.addRange(left,right)
    # # [6-7) [8-9)
    # left, right = [1, 3]
    # obj.removeRange(left,right)
    # # [6-7) [8-9)
    # left, right = [1, 8]
    # obj.addRange(left,right)
    # # [1-9)
    # print(obj.intervals)

    # obj = RangeModule()
    # obj.addRange(5, 8)
    # assert not obj.queryRange(3, 4)
    # obj.removeRange(5, 6)
    # obj.removeRange(3, 6)
    # obj.addRange(1, 3)
    # assert obj.queryRange(2, 3)