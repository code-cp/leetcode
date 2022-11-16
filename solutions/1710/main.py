from typing import * 

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        i = res = 0 
        while i < len(boxTypes) and truckSize > 0: 
            res += min(truckSize, boxTypes[i][0]) * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1 
        return res 

if __name__ == "__main__": 
    s = Solution()

    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    assert s.maximumUnits(boxTypes, truckSize) == 8
