from typing import * 

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n 
        for i in range(n): 
            for j, b in enumerate(boxes):
                if i == j: 
                    continue 
                if b != "1": 
                    continue 
                res[i] += abs(i-j)
        return res 

if __name__ == "__main__": 
    s = Solution() 

    boxes = "110"
    assert s.minOperations(boxes) == [1,1,3]

