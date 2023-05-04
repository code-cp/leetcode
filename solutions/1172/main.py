from sortedcontainers import SortedSet
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.not_full = SortedSet()

    def push(self, val: int) -> None:
        if len(self.not_full) == 0: 
            # all full, create a new set 
            self.stacks.append([val])    
            if self.capacity > 1: 
                self.not_full.add(len(self.stacks)-1)  
        else:
            # select the left most stack 
            idx = self.not_full[0]      
            self.stacks[idx].append(val)
            if len(self.stacks[idx]) == self.capacity: 
                self.not_full.discard(idx)
    
    def pop(self) -> int:
        idx = len(self.stacks)-1
        return self.popAtStack(idx)
    
    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or len(self.stacks[index]) == 0: 
            # cannot pop 
            return -1 
        
        val = self.stacks[index].pop()
        if index == len(self.stacks)-1 and len(self.stacks[-1]) == 0: 
            while len(self.stacks) > 0 and len(self.stacks[-1]) == 0: 
                self.not_full.discard(len(self.stacks)-1)
                self.stacks.pop()
        else: 
            self.not_full.add(index)
            
        return val  

if __name__ == "__main__": 
    s = DinnerPlates(1)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.popAtStack(1) == 2 
    assert s.pop() == 3
    assert s.pop() == 1 