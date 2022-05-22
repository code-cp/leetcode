from collections import deque, defaultdict
import random 
class RandomizedSet:

    def __init__(self):
        self.vec = deque() 
        self.hash_map = defaultdict(int) 

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        
        self.vec.append(val)
        self.hash_map[val] = len(self.vec) - 1
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.hash_map: 
            return False 

        idx = self.hash_map[val]
        last_val = self.vec[-1] 
 
        self.vec[idx] = last_val 
        self.vec.pop()
        
        # NOTE, this line should be before del 
        self.hash_map[last_val] = idx

        del self.hash_map[val] 

        return True 

    def getRandom(self) -> int:
        return self.vec[random.randint(0, len(self.vec) - 1)]

if __name__ == "__main__": 
    obj = RandomizedSet()
    assert obj.insert(1)
    assert not obj.remove(2)
    assert obj.insert(2)
    print(obj.getRandom())
    assert obj.remove(1)
    assert not obj.insert(2)
    assert obj.getRandom() == 2 