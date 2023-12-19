class CountIntervals:

    def __init__(self):
        # (left, right)
        self.intervals = []
        self.count_int = 0 

    def bsearch_left(self, target):
        # find the last interval whose left <= target 
        l, r = 0, len(self.intervals)-1
        while l <= r: 
            mid = ((r-l) >> 1) + l 
            if self.intervals[mid][0] <= target: 
                l = mid + 1
            else:
                r = mid - 1
        return max(0, r)
        
    def bsearch_right(self, target): 
        # find the first interval whose right >= target 
        l, r = 0, len(self.intervals)-1
        while l <= r: 
            mid = ((r-l) >> 1) + l
            if self.intervals[mid][1] < target: 
                l = mid + 1
            else:
                r = mid - 1
        return min(len(self.intervals)-1, l)
        
    def add(self, left: int, right: int) -> None:
        if len(self.intervals) == 0: 
            self.intervals.append([left, right])
            self.count_int += right - left + 1 
            return 
        
        left_idx = self.bsearch_left(left)
        right_idx = self.bsearch_right(right)
        
        # check overlap 
        if self.intervals[left_idx][1] < left: 
            left_idx += 1 
        if left_idx <= len(self.intervals) - 1: 
            left = min(left, self.intervals[left_idx][0])
        
        if self.intervals[right_idx][0] > right:
            right_idx -= 1 
        if right_idx >= 0:
            right = max(right, self.intervals[right_idx][1])
            
        # remove intervals 
        for i in range(left_idx, right_idx+1):
            if i < 0 or i > len(self.intervals) - 1: 
                continue 
            self.count_int -= self.intervals[i][1] - self.intervals[i][0] + 1
        for _ in range(left_idx, right_idx+1): 
            # NOTE, cannot del i, since after del intervals will change 
            del self.intervals[left_idx]

        self.count_int += right - left + 1 
        self.intervals.insert(left_idx, [left, right])

    def count(self) -> int:
        return self.count_int 

if __name__ == "__main__": 
    # obj = CountIntervals()
    # obj.add(2,3)
    # obj.add(7,10)
    # assert obj.count() == 6 
    # obj.add(5,8)
    # assert obj.count() == 8 

    # obj = CountIntervals()
    # print(obj.count())  # Output: 0
    # obj.add(8, 43)
    # obj.add(13, 16)
    # obj.add(26, 33)
    # obj.add(28, 36)
    # obj.add(29, 37)
    # print(obj.count())  # Output: 36
    # obj.add(34, 46)
    # obj.add(10, 23)

    obj = CountIntervals()
    obj.add(2,3)
    obj.add(2,3)
    obj.add(1,5)
    assert obj.count() == 5
