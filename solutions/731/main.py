# 和方法一：直接遍历的区别
# 1. 显式维护了根据start从小到大排列的区间
# 2. 使用二分寻找对应的插入位置
# 执行用时： 612 ms , 在所有 Python3 提交中击败了 62.04% 的用户
class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.double_booked = []

    @staticmethod
    def bsearch(start, end, events):
        n = len(events)
        if n == 0: 
            return 0 
        l, r = 0, n-1 
        while l <= r: 
            mid = (r-l)//2 + l 
            val = events[mid][0]
            if val <= end: 
                l = mid+1 
            elif val > end: 
                r = mid-1
        return l 

    @staticmethod
    def checkOverlap(start1, end1, start2, end2): 
        if start1 > end2 or end1 < start2: 
            return [-1, -1]  
        return [max(start1, start2), min(end1, end2)]  

    def book(self, start: int, end: int) -> bool:
        # change [s, e) to [s, e-1] 
        end -= 1 
        # check if overlap with double booked intervals 
        if len(self.double_booked) > 0:
            l2 = self.bsearch(start, end, self.double_booked)
            start2, end2 = self.double_booked[l2-1]
            if start2 <= end and end2 >= start: 
                return False 

        # update booked and double booked 
        l1 = self.bsearch(start, end, self.booked)
        if len(self.booked) == 0:
            self.booked.insert(l1, [start, end])
            return True 
        # update double booked 
        if l1 >= 1:
            id1 = l1 
            start1, end1 = self.booked[id1-1]
            while start1 <= end:
                interval = self.checkOverlap(start, end, start1, end1)
                if interval[0] != -1:
                    l2 = self.bsearch(*interval, self.double_booked)
                    if l2 == 0:
                        self.double_booked.insert(l2, interval)
                    else: 
                        # l2 > 0 
                        start2, end2 = self.double_booked[l2-1]
                        if l2 != 0 and start2 < self.double_booked[l2-1][0]:
                            l2 -= 1 
                        self.double_booked.insert(l2, interval)
                id1 -= 1 
                if id1 < 1:
                    break 
                start1, end1 = self.booked[id1-1]
        # update booked 
        if l1 != 0 and start < self.booked[l1-1][0]:
            l1 -= 1 
        self.booked.insert(l1, [start, end])
        return True 


if __name__ == "__main__": 
    myCalendar = MyCalendarTwo()
    assert myCalendar.book(10, 20)
    assert myCalendar.book(50, 60)
    assert myCalendar.book(10, 40)
    assert not myCalendar.book(5, 15)
    assert myCalendar.book(5, 10)
    assert myCalendar.book(25, 55)

    # # ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
    # # [[],[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
    myCalendar = MyCalendarTwo()
    assert myCalendar.book(26,35)
    assert myCalendar.book(26,32)
    assert not myCalendar.book(25,32)
    assert myCalendar.book(18,26)

    # # ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
    # # [[],[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
    myCalendar = MyCalendarTwo()
    assert myCalendar.book(24,40)
    assert myCalendar.book(43,50)
    assert myCalendar.book(27,43)
    assert myCalendar.book(5,21)
    assert not myCalendar.book(30,40)

    # ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
    # [[],[28,46],[9,21],[21,39],[37,48],[38,50],[22,39],[45,50],[1,12],[40,50],[31,44]]
    myCalendar = MyCalendarTwo()
    assert myCalendar.book(28,46)
    assert myCalendar.book(9,21)
    assert myCalendar.book(21,39)
    assert not myCalendar.book(37,48)
    assert not myCalendar.book(38,50)

    assert not myCalendar.book(22,39)
    assert myCalendar.book(45,50)
    assert myCalendar.book(1,12)
    assert not myCalendar.book(40,50)
    assert not myCalendar.book(31,44)

    # ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
    # [[],[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
    # [null,true,true,true,true,false,false,true,false,false,false]
    myCalendar = MyCalendarTwo()
    assert myCalendar.book(24,40)
    assert myCalendar.book(43,50)
    assert myCalendar.book(27,43)
    assert myCalendar.book(5,21)
    assert not myCalendar.book(30,40)

    assert not myCalendar.book(14,29)
    assert myCalendar.book(3,19)
    assert not myCalendar.book(3,14)
    assert not myCalendar.book(25,39)
    assert not myCalendar.book(6,19)