class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        end -= 1 
        n = len(self.events)
        if n == 0: 
            self.events.append([start, end])
            return True 
        l, r = 0, n-1 
        while l <= r: 
            mid = (r-l)//2 + l 
            val = self.events[mid][0]
            # NOTE, not end < val, the target is end, not val 
            if val < end: 
                l = mid+1 
            elif val > end: 
                r = mid-1
            else: 
                return False 
        if l > 0 and self.events[l-1][1] >= start:
            return False 
        self.events.insert(l, [start, end])
        return True 

if __name__ == "__main__": 

    # myCalendar = MyCalendar()
    # assert myCalendar.book(10, 20)
    # assert not myCalendar.book(15, 25)
    # assert myCalendar.book(20, 30)

    myCalendar = MyCalendar()
    assert myCalendar.book(47,50)
    assert myCalendar.book(33,41)
    assert not myCalendar.book(39,45)

