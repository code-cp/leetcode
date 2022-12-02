from typing import * 

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n 
        total = 1 if boxes[0] == "1" else 0 
        for i in range(1, n): 
            if boxes[i] == "0":
                continue 
            res[0] += i 
            total += 1 
        left = 1 if boxes[0] == "1" else 0
        for i in range(1, n): 
            diff = left - (total-left)
            res[i] = res[i-1] + diff 
            if boxes[i] == "1": 
                left += 1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    boxes = "110"
    assert s.minOperations(boxes) == [1,1,3]

