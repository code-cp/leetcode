from typing import * 

# ref https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/

from collections import OrderedDict 

class LRUCache: 
    def __init__(self, capacity: int): 
        self.cache = OrderedDict()
        self.capacity = capacity 
        self.total = 0 
        self.pre_key = -1 
        self.pre_num = 0 

    def add_value(self, key): 
        self.total += 1 
        if key not in self.cache: 
            self.cache[key] = 1 
        else: 
            if key != self.pre_key: 
                self.pre_num = self.cache[key] 
            self.cache[key] += 1 
        self.cache.move_to_end(key)
        self.pre_key = key 
        if len(self.cache) > self.capacity: 
            kv = self.cache.popitem(last = False)
            self.total -= kv[1]
            first = list(self.cache.keys())[0]
            self.cache[first] -= self.pre_num
            self.total -= self.pre_num
            self.pre_num = 0 

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        bucket = LRUCache(2)
        for f in fruits: 
            bucket.add_value(f)
            res = max(res, bucket.total)
        return res 

if __name__ == "__main__": 
    s = Solution() 

    fruits = [1,9,1,8,22,0,22,19,19,2,19,6,6,19,2,20,2,9,9,9,9,16,19,16,19,11,19,0,19,19]
    assert s.totalFruit(fruits) == 5   

    fruits = [0,1,6,6,4,4,6]
    assert s.totalFruit(fruits) == 5   

    fruits = [1,0,3,4,3]
    assert s.totalFruit(fruits) == 3 

    fruits = [1,0,1,4,1,4,1,2,3]
    assert s.totalFruit(fruits) == 5

    fruits = [0,1,2,2]
    assert s.totalFruit(fruits) == 3 

    fruits = [1,2,1]
    assert s.totalFruit(fruits) == 3 