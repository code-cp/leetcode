from collections import defaultdict 
class DinnerPlates:

    def __init__(self, capacity: int):
        self.left_not_full = 0
        self.right_not_empty = -1 
        self.capacity = capacity
        self.plates = defaultdict(list)

    def push(self, val: int) -> None:
        self.plates[self.left_not_full].append(val)
        while len(self.plates[self.left_not_full]) == self.capacity:
            self.left_not_full += 1 

        if len(self.plates[self.left_not_full]) != 0: 
            self.right_not_empty = max(self.right_not_empty, self.left_not_full)
        else: 
            self.right_not_empty = max(self.right_not_empty, self.left_not_full-1)
            
    
    def pop(self) -> int:
        if self.right_not_empty == -1: 
            return -1 
        return self.popAtStack(self.right_not_empty)
    
    def popAtStack(self, index: int) -> int:
        if len(self.plates[index]) == 0: 
            return -1 
    
        val = self.plates[index].pop()
        if index == self.right_not_empty and len(self.plates[index]) == 0: 
            while len(self.plates[self.right_not_empty]) == 0 and self.right_not_empty >= 0: 
                self.right_not_empty -= 1 
    
        self.left_not_full = min(self.left_not_full, index)
    
        return val 

if __name__ == "__main__": 
    s = DinnerPlates(1)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.popAtStack(1) == 2 
    assert s.pop() == 3
    assert s.pop() == 1 